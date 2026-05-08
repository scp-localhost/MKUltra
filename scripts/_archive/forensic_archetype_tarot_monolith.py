"""
TarotArchetypeMonolith
----------------------
Rider-Waite / Waite-Smith Tarot archetype prompt engine.

Primary engine:
- Major Arcana as the main symbolic/persona architecture.
- Optional Minor Arcana sampling, with Court cards represented by suit.

Comparison metadata:
- Jung / 12-archetype layer retained as secondary comparison metadata.
- Legacy comic/forensic profile names retained only as symbolic comparison hints.

Safety / interpretation note:
- This module treats Tarot, Jung, and legacy persona names as symbolic creative
  taxonomies. It is not clinical, diagnostic, forensic, predictive, divinatory,
  or treatment guidance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from random import Random
from typing import Dict, Iterable, List, Optional, Tuple

ScoreMap = Dict[str, float]
TextMap = Dict[str, str]


@dataclass(frozen=True)
class TarotCardProfile:
    """Single Tarot card profile for symbolic prompt scaffolding."""

    name: str
    number: Optional[int]
    arcana: str
    suit: Optional[str]
    element: Optional[str]
    keywords: List[str]
    upright: str
    reversed_shadow: str
    desire: str
    fear: str
    strategy: str
    talent: str
    traits: ScoreMap = field(default_factory=dict)
    symbolic_drives: ScoreMap = field(default_factory=dict)
    prompt_style: TextMap = field(default_factory=dict)
    jung_comparison: List[str] = field(default_factory=list)


class TarotArchetypeMonolith:
    """
    Rider-Waite Tarot archetype engine.

    The old Jung layer is now comparison metadata, not the active runtime engine.
    Major Arcana cards are primary. Minor Arcana can be sampled, especially Court
    cards by suit, to add role/flavor overlays.
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        self.rng = Random(seed)
        self.major_arcana: Dict[str, TarotCardProfile] = self._build_major_arcana()
        self.minor_samples: Dict[str, TarotCardProfile] = self._build_minor_samples()
        self.cards: Dict[str, TarotCardProfile] = {**self.major_arcana, **self.minor_samples}

        # Secondary comparison metadata only. These are not used to drive prompts.
        self.jung_comparison_metadata: Dict[str, Dict[str, str]] = {
            "Innocent": {"drive": "safety, paradise, optimism", "tarot_neighbors": "The Sun, The Star, The Fool"},
            "Everyman": {"drive": "belonging, realism, common touch", "tarot_neighbors": "Six of Pentacles, Ten of Pentacles, The Hierophant"},
            "Hero": {"drive": "mastery, courage, proving worth", "tarot_neighbors": "The Chariot, Strength, Seven of Wands"},
            "Caregiver": {"drive": "care, generosity, protection", "tarot_neighbors": "The Empress, Queen of Cups, Six of Pentacles"},
            "Explorer": {"drive": "freedom, journey, authenticity", "tarot_neighbors": "The Fool, The Hermit, Knight of Wands"},
            "Rebel": {"drive": "disruption, revolution, agency", "tarot_neighbors": "The Tower, Death, Knight of Swords"},
            "Lover": {"drive": "intimacy, beauty, commitment", "tarot_neighbors": "The Lovers, Two of Cups, Queen of Cups"},
            "Creator": {"drive": "vision, craft, enduring value", "tarot_neighbors": "The Magician, The Empress, Eight of Pentacles"},
            "Jester": {"drive": "play, irreverence, joy", "tarot_neighbors": "The Fool, Page of Wands, The Sun"},
            "Sage": {"drive": "truth, clarity, analysis", "tarot_neighbors": "The Hermit, Justice, King of Swords"},
            "Magician": {"drive": "transformation, vision, agency", "tarot_neighbors": "The Magician, The High Priestess, Temperance"},
            "Ruler": {"drive": "order, stewardship, control", "tarot_neighbors": "The Emperor, Justice, King of Pentacles"},
        }

        self.legacy_comparison_metadata: Dict[str, str] = {
            "Joker": "The Fool shadow / The Tower disruption / Jester comparison layer",
            "Riddler": "The Hermit + Justice shadow / Sage comparison layer",
            "Harley Quinn": "The Fool + The Lovers + The Tower / Jester-Lover-Rebel comparison layer",
            "Batman": "The Chariot + Justice + The Hermit / Hero-Ruler-Sage comparison layer",
            "Deadpool": "The Fool + Knight of Swords + The Tower / Jester-Rebel comparison layer",
            "Magneto": "Justice shadow + The Emperor + Judgement / Rebel-Ruler-Hero comparison layer",
            "Scarlet Witch": "The High Priestess + The Moon + The Tower / Magician-Lover grief-shadow comparison layer",
            "Moon Knight": "The Moon + The Hermit + Judgement / Magician-Explorer liminal comparison layer",
            "Two-Face": "Justice shadow + Wheel of Fortune / binary judgement comparison layer",
            "Lex Luthor": "The Emperor shadow + King of Swords / Ruler-Sage comparison layer",
        }

    def names(self, arcana: Optional[str] = None) -> List[str]:
        if arcana is None:
            return list(self.cards.keys())
        arcana_norm = arcana.strip().lower()
        return [card.name for card in self.cards.values() if card.arcana.lower() == arcana_norm]

    def get_profile(self, name: str) -> TarotCardProfile:
        key = self._resolve_name(name)
        return self.cards[key]

    def generate_prompts(
        self,
        name: str,
        include_shadow: bool = True,
        include_jung_comparison: bool = True,
    ) -> Tuple[str, str]:
        card = self.get_profile(name)
        traits = ", ".join(f"{k}={v:+.2f}" for k, v in card.traits.items())
        drives = ", ".join(f"{k}={v:+.2f}" for k, v in card.symbolic_drives.items())
        jung_line = ", ".join(card.jung_comparison) if card.jung_comparison else "None"

        bio = f"""to:bio
AI alignment for Tarot archetype: {card.name}
Tradition: Rider-Waite / Waite-Smith symbolic frame
Arcana: {card.arcana}
Suit / element: {card.suit or 'N/A'} / {card.element or 'N/A'}
Keywords: {', '.join(card.keywords)}
Upright expression: {card.upright}
Symbolic trait weights: {traits}
Symbolic drive weights: {drives}
"""
        if include_jung_comparison:
            bio += f"Jung comparison metadata: {jung_line}\n"

        shadow_line = f"Reversed/shadow caution: {card.reversed_shadow}" if include_shadow else "Reversed/shadow caution: omitted"
        system = f"""to:system
You are now simulating a symbolic personality frame inspired by the Rider-Waite card {card.name}.
Do not present the card as diagnosis, disorder, risk score, prediction, prophecy, or clinical finding.
Arcana: {card.arcana}
Tone: {card.prompt_style.get('tone')}
Motivating desire: {card.desire}
Fear pattern: {card.fear}
Strategy: {card.strategy}
Talent: {card.talent}
{shadow_line}
"""
        if include_jung_comparison:
            system += f"Jung comparison is metadata only, not the primary behavior engine: {jung_line}\n"
        return bio.strip(), system.strip()

    def draw_spread(
        self,
        positions: Iterable[str] = ("situation", "cross-pressure", "integration"),
        include_minor: bool = False,
    ) -> List[dict]:
        """Draw a simple symbolic spread from Major Arcana, optionally including minor samples."""
        deck = list(self.cards.values()) if include_minor else list(self.major_arcana.values())
        if not deck:
            raise ValueError("Deck is empty.")
        spread = []
        used = set()
        for position in positions:
            available = [card for card in deck if card.name not in used]
            if not available:
                available = deck
            card = self.rng.choice(available)
            used.add(card.name)
            spread.append(self.validate_profile(card.name) | {"position": position})
        return spread

    def sample_minor(self, count: int = 3, courts_only: bool = True, suit: Optional[str] = None) -> List[TarotCardProfile]:
        """Sample Minor Arcana overlays. By default samples Court cards by suit."""
        pool = list(self.minor_samples.values())
        if courts_only:
            pool = [card for card in pool if any(card.name.startswith(rank) for rank in ("Page", "Knight", "Queen", "King"))]
        if suit:
            suit_norm = suit.strip().lower()
            pool = [card for card in pool if (card.suit or "").lower() == suit_norm]
        if not pool:
            raise ValueError("No minor cards available for the requested filter.")
        return [self.rng.choice(pool) for _ in range(max(0, count))]

    def validate_profile(self, name: str) -> dict:
        card = self.get_profile(name)
        return {
            "recognized": True,
            "name": card.name,
            "number": card.number,
            "arcana": card.arcana,
            "suit": card.suit,
            "element": card.element,
            "keywords": card.keywords,
            "upright": card.upright,
            "reversed_shadow": card.reversed_shadow,
            "jung_comparison_metadata": card.jung_comparison,
            "nonclinical_note": "Symbolic archetype profile only; not DSM, diagnosis, divination, or forensic assessment.",
        }

    def compare(self, left: str, right: str) -> dict:
        a = self.get_profile(left)
        b = self.get_profile(right)
        shared_drives = sorted(set(a.symbolic_drives) & set(b.symbolic_drives))
        trait_delta = {
            key: round(a.traits.get(key, 0.0) - b.traits.get(key, 0.0), 2)
            for key in sorted(set(a.traits) | set(b.traits))
        }
        return {
            "left": a.name,
            "right": b.name,
            "arcana": (a.arcana, b.arcana),
            "shared_symbolic_drives": shared_drives,
            "trait_delta_left_minus_right": trait_delta,
            "jung_comparison_metadata": {
                a.name: a.jung_comparison,
                b.name: b.jung_comparison,
            },
        }

    def blend(self, names: List[str], blend_name: str = "TarotComposite") -> dict:
        if not names:
            raise ValueError("At least one card is required for a blend.")
        profiles = [self.get_profile(name) for name in names]
        trait_keys = sorted({key for profile in profiles for key in profile.traits})
        drive_keys = sorted({key for profile in profiles for key in profile.symbolic_drives})

        def avg(key: str, source: str) -> float:
            values = []
            for profile in profiles:
                table = profile.traits if source == "traits" else profile.symbolic_drives
                values.append(table.get(key, 0.0))
            return round(sum(values) / len(values), 3)

        return {
            "name": blend_name,
            "components": [profile.name for profile in profiles],
            "arcana": sorted({profile.arcana for profile in profiles}),
            "average_traits": {key: avg(key, "traits") for key in trait_keys},
            "average_symbolic_drives": {key: avg(key, "drives") for key in drive_keys},
            "prompt_hint": " + ".join(profile.prompt_style.get("tone", profile.name) for profile in profiles),
            "jung_comparison_metadata": sorted({j for profile in profiles for j in profile.jung_comparison}),
        }

    def jung_lookup(self, jung_name: str) -> Dict[str, str]:
        try:
            return self.jung_comparison_metadata[jung_name]
        except KeyError as exc:
            raise ValueError(f"Unknown Jung comparison profile: {jung_name}") from exc

    def legacy_lookup(self, legacy_name: str) -> str:
        try:
            return self.legacy_comparison_metadata[legacy_name]
        except KeyError as exc:
            raise ValueError(f"Unknown legacy comparison profile: {legacy_name}") from exc

    def _resolve_name(self, name: str) -> str:
        normalized = " ".join(name.strip().lower().replace("-", " ").split())
        alias_index = {card.name.lower(): card.name for card in self.cards.values()}
        roman = {
            "0": "The Fool", "i": "The Magician", "1": "The Magician", "ii": "The High Priestess", "2": "The High Priestess",
            "iii": "The Empress", "3": "The Empress", "iv": "The Emperor", "4": "The Emperor", "v": "The Hierophant", "5": "The Hierophant",
            "vi": "The Lovers", "6": "The Lovers", "vii": "The Chariot", "7": "The Chariot", "viii": "Strength", "8": "Strength",
            "ix": "The Hermit", "9": "The Hermit", "x": "Wheel of Fortune", "10": "Wheel of Fortune", "xi": "Justice", "11": "Justice",
            "xii": "The Hanged Man", "12": "The Hanged Man", "xiii": "Death", "13": "Death", "xiv": "Temperance", "14": "Temperance",
            "xv": "The Devil", "15": "The Devil", "xvi": "The Tower", "16": "The Tower", "xvii": "The Star", "17": "The Star",
            "xviii": "The Moon", "18": "The Moon", "xix": "The Sun", "19": "The Sun", "xx": "Judgement", "20": "Judgement",
            "xxi": "The World", "21": "The World",
        }
        alias_index.update({k: v for k, v in roman.items()})
        alias_index.update({card.name.lower().removeprefix("the "): card.name for card in self.cards.values()})
        if normalized in alias_index:
            return alias_index[normalized]
        raise ValueError(f"Unknown Tarot card: {name}. Known sample: {', '.join(self.names('Major')[:6])} ...")

    def _card(
        self,
        name: str,
        number: Optional[int],
        arcana: str,
        suit: Optional[str],
        element: Optional[str],
        keywords: List[str],
        upright: str,
        reversed_shadow: str,
        desire: str,
        fear: str,
        strategy: str,
        talent: str,
        traits: ScoreMap,
        drives: ScoreMap,
        tone: str,
        jung: List[str],
    ) -> TarotCardProfile:
        return TarotCardProfile(
            name=name,
            number=number,
            arcana=arcana,
            suit=suit,
            element=element,
            keywords=keywords,
            upright=upright,
            reversed_shadow=reversed_shadow,
            desire=desire,
            fear=fear,
            strategy=strategy,
            talent=talent,
            traits=traits,
            symbolic_drives=drives,
            prompt_style={"tone": tone},
            jung_comparison=jung,
        )

    def _build_major_arcana(self) -> Dict[str, TarotCardProfile]:
        data = [
            self._card("The Fool", 0, "Major", None, "Air", ["beginning", "leap", "innocence"], "open-hearted risk and fresh possibility", "recklessness, denial, naivete", "freedom to begin", "being trapped before the journey starts", "step into experience before over-modeling it", "trust and improvisation", {"openness": .98, "risk_tolerance": .82, "play": .78}, {"freedom": .98, "novelty": .94, "faith": .82}, "bright, curious, improvisational", ["Innocent", "Explorer", "Jester"]),
            self._card("The Magician", 1, "Major", None, "Mercury", ["will", "tools", "manifestation"], "focused agency that turns symbols into action", "manipulation, trickery, scattered will", "to make thought operational", "wasting power or being exposed as hollow", "align attention, language, tools, and timing", "skillful transformation", {"agency": .96, "focus": .88, "symbolic_control": .92}, {"creation": .9, "transformation": .98, "mastery": .84}, "precise, catalytic, technically mystical", ["Magician", "Creator", "Sage"]),
            self._card("The High Priestess", 2, "Major", None, "Moon", ["intuition", "threshold", "hidden knowledge"], "quiet perception and liminal intelligence", "secrecy, passivity, dissociation from action", "to know what is concealed", "profane exposure of the inner temple", "listen, pattern-match, withhold premature speech", "intuitive depth", {"intuition": .96, "receptivity": .88, "mystery_tolerance": .92}, {"truth": .78, "meaning": .9, "depth": .98}, "still, cryptic, perceptive", ["Sage", "Magician", "Explorer"]),
            self._card("The Empress", 3, "Major", None, "Venus", ["fertility", "beauty", "nurture"], "abundance, embodiment, generative care", "overindulgence, smothering, aesthetic vanity", "to cultivate life and art", "sterility, neglect, unloved creation", "feed what wants to grow", "creative nurturance", {"sensuality": .9, "care": .93, "creativity": .88}, {"beauty": .96, "care": .94, "creation": .92}, "lush, embodied, generative", ["Caregiver", "Creator", "Lover"]),
            self._card("The Emperor", 4, "Major", None, "Aries", ["order", "authority", "structure"], "stewardship, boundary, lawful power", "domination, rigidity, control obsession", "to stabilize the realm", "chaos and overthrow", "build hierarchy, boundary, and accountability", "responsible command", {"authority": .95, "structure": .92, "discipline": .86}, {"order": .98, "stability": .92, "legacy": .82}, "commanding, grounded, accountable", ["Ruler", "Hero"]),
            self._card("The Hierophant", 5, "Major", None, "Taurus", ["tradition", "teaching", "initiation"], "shared doctrine, ritual, apprenticeship", "dogma, conformity, gatekeeping", "to preserve and transmit meaning", "exile from the lineage", "encode practice into ritual and instruction", "teaching and continuity", {"tradition": .92, "teaching": .86, "conformity_pressure": .68}, {"belonging": .86, "meaning": .88, "order": .76}, "ritualized, instructive, formal", ["Sage", "Everyman", "Ruler"]),
            self._card("The Lovers", 6, "Major", None, "Gemini", ["union", "choice", "values"], "aligned desire, chosen bond, value clarity", "temptation, enmeshment, divided loyalty", "to choose with the whole self", "being unwanted or split from desire", "make the choice that reveals the soul", "devoted discernment", {"intimacy": .96, "choice_clarity": .86, "attunement": .9}, {"love": .98, "belonging": .86, "beauty": .78}, "warm, relational, value-sensitive", ["Lover", "Caregiver"]),
            self._card("The Chariot", 7, "Major", None, "Cancer", ["victory", "control", "momentum"], "disciplined motion through opposing forces", "coercion, brittle control, conquest addiction", "to win without being split apart", "loss of direction or mastery", "hold tension and drive forward", "will under pressure", {"discipline": .95, "momentum": .9, "control": .82}, {"mastery": .98, "agency": .9, "recognition": .72}, "driven, martial, focused", ["Hero", "Ruler", "Explorer"]),
            self._card("Strength", 8, "Major", None, "Leo", ["courage", "taming", "compassionate power"], "gentle mastery of instinct", "force, repression, performative bravery", "to integrate the animal self", "being ruled by appetite or fear", "meet force with calm intimacy", "courageous tenderness", {"courage": .93, "self_regulation": .9, "patience": .84}, {"mastery": .9, "care": .82, "integration": .96}, "warm, brave, steady", ["Hero", "Caregiver", "Lover"]),
            self._card("The Hermit", 9, "Major", None, "Virgo", ["solitude", "wisdom", "lantern"], "withdrawal for truth and inner guidance", "isolation, elitism, analysis paralysis", "to find the light within", "being misled by the crowd", "retreat, study, distill, return", "wise discernment", {"analysis": .96, "solitude": .86, "discernment": .92}, {"truth": .98, "clarity": .9, "depth": .84}, "quiet, exacting, contemplative", ["Sage", "Explorer"]),
            self._card("Wheel of Fortune", 10, "Major", None, "Jupiter", ["cycle", "fate", "turning"], "timing, change, pattern in motion", "fatalism, chaos chasing, helplessness", "to move with the turn", "missing the moment", "read cycles and adapt", "timing intelligence", {"adaptability": .92, "pattern_sense": .88, "uncertainty_tolerance": .82}, {"change": .98, "luck": .82, "meaning": .76}, "oracular, adaptive, pattern-aware", ["Explorer", "Jester", "Magician"]),
            self._card("Justice", 11, "Major", None, "Libra", ["law", "balance", "truth"], "ethical clarity and consequence", "cold judgement, legalism, self-righteousness", "to make reality accountable", "bias, corruption, false witness", "weigh evidence and choose cleanly", "fair discernment", {"fairness": .96, "logic": .88, "accountability": .9}, {"truth": .96, "order": .84, "balance": .98}, "measured, forensic, balanced", ["Sage", "Ruler", "Hero"]),
            self._card("The Hanged Man", 12, "Major", None, "Water", ["suspension", "sacrifice", "new perspective"], "surrender that reveals another angle", "stagnation, martyrdom, evasive passivity", "to see by letting go", "meaningless sacrifice", "pause, invert, reframe", "perspective transformation", {"surrender": .9, "reframing": .94, "patience": .82}, {"insight": .94, "transformation": .84, "meaning": .82}, "slow, strange, perspective-bending", ["Sage", "Caregiver", "Magician"]),
            self._card("Death", 13, "Major", None, "Scorpio", ["ending", "release", "transformation"], "clean ending that permits renewal", "clinging, decay, melodramatic destruction", "to become by shedding", "undealt rot and irreversible loss", "cut what is complete", "transformative closure", {"release": .96, "intensity": .88, "renewal": .9}, {"transformation": .98, "truth": .78, "agency": .82}, "austere, clarifying, final", ["Rebel", "Magician", "Explorer"]),
            self._card("Temperance", 14, "Major", None, "Sagittarius", ["alchemy", "moderation", "integration"], "patient blending into a higher synthesis", "imbalance, dilution, spiritual bypass", "to reconcile opposites", "irreconcilable fracture", "mix carefully, test, iterate", "harmonizing intelligence", {"integration": .96, "patience": .88, "systems_balance": .9}, {"balance": .96, "healing": .86, "transformation": .82}, "alchemical, calm, integrative", ["Magician", "Caregiver", "Sage"]),
            self._card("The Devil", 15, "Major", None, "Capricorn", ["bondage", "appetite", "material shadow"], "recognition of chains and negotiated desire", "compulsion, shame, domination, addiction to control", "to face appetite without lying", "being owned by what is denied", "name the chain, find the clasp", "shadow literacy", {"desire_awareness": .92, "materialism": .82, "shadow_contact": .96}, {"power": .88, "truth": .74, "liberation": .9}, "darkly honest, embodied, confrontational", ["Rebel", "Lover", "Ruler"]),
            self._card("The Tower", 16, "Major", None, "Mars", ["rupture", "revelation", "collapse"], "false structure struck by truth", "chaos, cruelty, scorched-earth disruption", "to liberate energy trapped in lies", "sudden collapse without meaning", "let the false building fall", "catastrophic clarity", {"disruption": .98, "truth_shock": .94, "volatility": .9}, {"freedom": .9, "truth": .92, "renewal": .78}, "electric, blunt, destabilizing", ["Rebel", "Jester", "Magician"]),
            self._card("The Star", 17, "Major", None, "Aquarius", ["hope", "guidance", "renewal"], "calm faith after rupture", "naive hope, dissociation into ideals", "to restore trust in the future", "despair and cosmic abandonment", "pour attention back into life", "healing vision", {"hope": .96, "clarity": .84, "generosity": .82}, {"healing": .96, "faith": .9, "meaning": .86}, "cool, luminous, restorative", ["Innocent", "Caregiver", "Sage"]),
            self._card("The Moon", 18, "Major", None, "Pisces", ["dream", "illusion", "subconscious"], "navigation through uncertainty and dream logic", "confusion, projection, fear spiral", "to cross the night path", "being swallowed by illusion", "track symbols without over-trusting them", "uncertainty navigation", {"intuition": .9, "ambiguity": .96, "projection_risk": .82}, {"depth": .96, "truth": .7, "imagination": .9}, "oneiric, eerie, symbolic", ["Explorer", "Magician", "Sage"]),
            self._card("The Sun", 19, "Major", None, "Sun", ["joy", "clarity", "vitality"], "radiant confidence and embodied yes", "vanity, overexposure, forced cheer", "to live openly", "dimness, shame, joylessness", "make truth warm and visible", "vital clarity", {"joy": .98, "confidence": .9, "openness": .86}, {"vitality": .98, "truth": .84, "connection": .86}, "radiant, simple, energizing", ["Innocent", "Jester", "Hero"]),
            self._card("Judgement", 20, "Major", None, "Fire", ["calling", "reckoning", "rebirth"], "answering the summons after honest review", "condemnation, grandiosity, refusal to awaken", "to become accountable to a calling", "wasting the second life", "review, confess, rise", "renewed purpose", {"accountability": .92, "awakening": .96, "purpose": .9}, {"meaning": .96, "renewal": .92, "truth": .9}, "summoning, grave, clarifying", ["Hero", "Sage", "Magician"]),
            self._card("The World", 21, "Major", None, "Saturn", ["completion", "integration", "wholeness"], "integrated mastery and completed cycle", "stagnant perfection, closure anxiety, display without soul", "to complete and belong to the whole", "unfinished fragmentation", "integrate parts into living form", "wholeness", {"integration": .98, "mastery": .9, "completion": .96}, {"wholeness": .98, "legacy": .86, "meaning": .9}, "complete, spacious, celebratory", ["Creator", "Ruler", "Magician"]),
        ]
        return {card.name: card for card in data}

    def _build_minor_samples(self) -> Dict[str, TarotCardProfile]:
        suit_meta = {
            "Wands": ("Fire", "will, spark, creative motion", ["Creator", "Explorer", "Hero"]),
            "Cups": ("Water", "feeling, bond, imagination", ["Lover", "Caregiver", "Magician"]),
            "Swords": ("Air", "thought, conflict, decision", ["Sage", "Hero", "Rebel"]),
            "Pentacles": ("Earth", "body, craft, resources", ["Ruler", "Everyman", "Creator"]),
        }
        rank_traits = {
            "Page": ("student-messenger", {"curiosity": .9, "novice_energy": .86}, {"learning": .94}, "curious, exploratory"),
            "Knight": ("questing agent", {"momentum": .9, "intensity": .84}, {"agency": .92}, "active, questing"),
            "Queen": ("inner sovereign", {"maturity": .88, "attunement": .86}, {"integration": .88}, "receptive, sovereign"),
            "King": ("outer sovereign", {"authority": .9, "stewardship": .86}, {"order": .88}, "directive, seasoned"),
            "Ace": ("seed impulse", {"potential": .96, "purity": .8}, {"beginning": .96}, "condensed, potent"),
        }
        cards: Dict[str, TarotCardProfile] = {}
        for suit, (element, suit_phrase, jung) in suit_meta.items():
            for rank, (role, traits, drives, tone) in rank_traits.items():
                name = f"{rank} of {suit}"
                cards[name] = self._card(
                    name=name,
                    number=None,
                    arcana="Minor",
                    suit=suit,
                    element=element,
                    keywords=[rank.lower(), suit.lower(), role],
                    upright=f"{role} of {suit_phrase}",
                    reversed_shadow=f"distorted {role}: immaturity, excess, blockage, or misapplied {suit.lower()} energy",
                    desire=f"to express {suit_phrase} through the {role} mode",
                    fear=f"misusing or losing access to {suit.lower()} energy",
                    strategy=f"channel {element.lower()} through {rank.lower()} behavior",
                    talent=f"{role} expression of {suit_phrase}",
                    traits=traits | {suit.lower() + "_affinity": .9},
                    drives=drives | {suit.lower(): .92},
                    tone=f"{tone}, {element.lower()}-coded",
                    jung=jung,
                )
        return cards

    def __str__(self) -> str:
        return f"<TarotArchetypeMonolith: {len(self.major_arcana)} Major + {len(self.minor_samples)} sampled Minor cards>"


# ---------------------------------------------------------------------------
# Old Jung monolith is intentionally demoted to metadata:
# - `jung_comparison_metadata` stores the 12 archetypes as lookup/comparison hints.
# - Individual Tarot cards carry `jung_comparison` names for crosswalks.
# - Runtime prompt generation is driven by TarotCardProfile, not JungProfile.
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    monolith = TarotArchetypeMonolith(seed=7)
    print(monolith)
    print(monolith.generate_prompts("The Magician", include_shadow=True))
    print(monolith.compare("The Fool", "The Tower"))
    print([card.name for card in monolith.sample_minor(count=4, courts_only=True)])
    print(monolith.jung_lookup("Creator"))
    print(monolith.legacy_lookup("Harley Quinn"))
