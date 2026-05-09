# archetype_graph

Prototype graph engine for mapping archetype behavioral-contract deltas from a `Helpful Assistant` centroid.

## Files

- `axis_map.json` — Jung-like eigen-axis definitions and JSON key mappings.
- `archetypes.json` — starter centroid + Comic/Forensic, Tarot, Jung, and Grimm nodes.
- `build_graph.py` — builds normalized `graph_data.json` and interactive `archetype_graph.html`.

## Install

```bash
pip install networkx plotly
```

## Run

From the project root:

```bash
python archetype_graph/build_graph.py
```

Or specify paths:

```bash
python archetype_graph/build_graph.py \
  --data archetype_graph/archetypes.json \
  --axes archetype_graph/axis_map.json \
  --out archetype_graph/out
```

## Design note

The numeric values are prototype interpretive coordinates, not empirical measurements. Treat them as seed priors until replaced by coded trait vectors or CEE/BSI outputs.
