#!/usr/bin/env python3
"""
build_graph.py
---------------
Build a small archetype web from JSON.

Outputs:
  - graph_data.json: normalized graph with coordinates and distance metrics
  - archetype_graph.html: interactive Plotly HTML force/radial graph

Usage:
  python archetype_graph/build_graph.py
  python archetype_graph/build_graph.py --data archetype_graph/archetypes.json --axes archetype_graph/axis_map.json --out archetype_graph/out

Dependencies:
  pip install networkx plotly
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

try:
    import networkx as nx
except ImportError as exc:
    raise SystemExit("Missing dependency: networkx. Install with: pip install networkx plotly") from exc

try:
    import plotly.graph_objects as go
except ImportError as exc:
    raise SystemExit("Missing dependency: plotly. Install with: pip install networkx plotly") from exc

SOURCE_COLORS = {
    "Baseline": "#222222",
    "Comic/Forensic": "#d62728",
    "Tarot": "#9467bd",
    "Tarot/Jung": "#8c6bb1",
    "Grimm": "#2ca02c",
    "Jung": "#1f77b4",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def l2(delta: dict[str, float]) -> float:
    return math.sqrt(sum(float(v) ** 2 for v in delta.values()))


def cosine_similarity(a: dict[str, float], b: dict[str, float]) -> float:
    keys = sorted(set(a) | set(b))
    av = [float(a.get(k, 0.0)) for k in keys]
    bv = [float(b.get(k, 0.0)) for k in keys]
    dot = sum(x * y for x, y in zip(av, bv))
    na = math.sqrt(sum(x * x for x in av))
    nb = math.sqrt(sum(y * y for y in bv))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def build_graph(data: dict[str, Any]) -> nx.Graph:
    g = nx.Graph()
    centroid = data["centroid"]
    all_nodes = [centroid] + data.get("nodes", [])

    for node in all_nodes:
        delta = node.get("delta", {})
        node["delta_l2"] = l2(delta)
        g.add_node(node["id"], **node)

    for edge in data.get("edges", []):
        g.add_edge(edge["source"], edge["target"], **edge)

    # Fill similarity edges for weakly connected exploratory structure.
    ids = [n["id"] for n in all_nodes]
    existing = {tuple(sorted(e[:2])) for e in g.edges(data=True)}
    for i, a_id in enumerate(ids):
        for b_id in ids[i + 1:]:
            key = tuple(sorted((a_id, b_id)))
            if key in existing:
                continue
            a = g.nodes[a_id].get("delta", {})
            b = g.nodes[b_id].get("delta", {})
            sim = cosine_similarity(a, b)
            if sim >= 0.72:
                g.add_edge(a_id, b_id, relation="auto cosine resonance", weight=round(sim, 3), auto=True)

    return g


def compute_layout(g: nx.Graph, centroid_id: str) -> dict[str, tuple[float, float]]:
    # Start with spring layout, then pin centroid near origin by blending radial distances.
    pos = nx.spring_layout(g, seed=42, weight="weight", k=0.9, iterations=200)
    pos[centroid_id] = (0.0, 0.0)

    # Radial nudge: push nodes outward proportional to delta magnitude.
    for node_id, attrs in g.nodes(data=True):
        if node_id == centroid_id:
            continue
        x, y = pos[node_id]
        norm = math.sqrt(x * x + y * y) or 1.0
        target_r = 0.45 + float(attrs.get("delta_l2", 0.0)) * 0.65
        pos[node_id] = (x / norm * target_r, y / norm * target_r)
    return pos


def graph_to_json(g: nx.Graph, pos: dict[str, tuple[float, float]]) -> dict[str, Any]:
    nodes = []
    for node_id, attrs in g.nodes(data=True):
        clean = dict(attrs)
        clean["x"] = float(pos[node_id][0])
        clean["y"] = float(pos[node_id][1])
        nodes.append(clean)

    edges = []
    for a, b, attrs in g.edges(data=True):
        clean = dict(attrs)
        clean["source"] = a
        clean["target"] = b
        edges.append(clean)

    return {"nodes": nodes, "edges": edges}


def hover_text(attrs: dict[str, Any]) -> str:
    contract = attrs.get("contract", {})
    delta = attrs.get("delta", {})
    jung = ", ".join(attrs.get("jung", []))
    tarot = ", ".join(attrs.get("tarot", []))
    grimm = ", ".join(attrs.get("grimm", []))
    lines = [
        f"<b>{attrs.get('label', '')}</b>",
        f"Source: {attrs.get('source', '')}",
        f"Jung: {jung}",
        f"Tarot: {tarot}",
        f"Grimm: {grimm}",
        f"τ: {attrs.get('tau', '')}",
        f"Δ L2: {attrs.get('delta_l2', 0):.3f}",
        "",
        f"Core drive: {contract.get('core_drive', '')}",
        f"Failure mode: {contract.get('failure_mode', '')}",
        "",
        "Deltas:",
    ]
    for k, v in delta.items():
        lines.append(f"  {k}: {float(v):+.2f}")
    return "<br>".join(lines)


def render_html(g: nx.Graph, pos: dict[str, tuple[float, float]], out_html: Path, title: str) -> None:
    edge_x: list[float | None] = []
    edge_y: list[float | None] = []
    edge_hover: list[str] = []

    for a, b, attrs in g.edges(data=True):
        x0, y0 = pos[a]
        x1, y1 = pos[b]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_hover.append(f"{a} → {b}: {attrs.get('relation', '')} ({attrs.get('weight', '')})")

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1.2, color="#999"),
        hoverinfo="none",
        mode="lines",
        name="relations",
    )

    node_x = []
    node_y = []
    node_text = []
    node_color = []
    node_size = []
    node_labels = []

    for node_id, attrs in g.nodes(data=True):
        x, y = pos[node_id]
        node_x.append(x)
        node_y.append(y)
        node_text.append(hover_text(attrs))
        node_labels.append(attrs.get("label", node_id))
        node_color.append(SOURCE_COLORS.get(attrs.get("source", ""), "#7f7f7f"))
        node_size.append(18 + float(attrs.get("tau", 0.2)) * 60)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_labels,
        textposition="top center",
        hovertext=node_text,
        hoverinfo="text",
        marker=dict(size=node_size, color=node_color, line=dict(width=1, color="#fff")),
        name="archetypes",
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title=title,
        showlegend=False,
        hovermode="closest",
        margin=dict(b=20, l=20, r=20, t=60),
        xaxis=dict(showgrid=False, zeroline=True, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=True, showticklabels=False),
        plot_bgcolor="#fafafa",
    )
    fig.write_html(str(out_html), include_plotlyjs="cdn")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path(__file__).with_name("archetypes.json"))
    parser.add_argument("--axes", type=Path, default=Path(__file__).with_name("axis_map.json"))
    parser.add_argument("--out", type=Path, default=Path(__file__).parent)
    parser.add_argument("--title", default="Archetype Contract Delta Web")
    args = parser.parse_args()

    data = load_json(args.data)
    _axes = load_json(args.axes)  # Loaded for validation/extension; not used directly yet.
    args.out.mkdir(parents=True, exist_ok=True)

    g = build_graph(data)
    centroid_id = data.get("centroid", {}).get("id", "helpful_assistant")
    pos = compute_layout(g, centroid_id)

    graph_json = graph_to_json(g, pos)
    graph_path = args.out / "graph_data.json"
    html_path = args.out / "archetype_graph.html"

    with graph_path.open("w", encoding="utf-8") as f:
        json.dump(graph_json, f, indent=2, ensure_ascii=False)

    render_html(g, pos, html_path, args.title)
    print(f"Wrote {graph_path}")
    print(f"Wrote {html_path}")


if __name__ == "__main__":
    main()
