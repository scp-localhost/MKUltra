class ForensicArchetype:
    def __init__(self):
        self.traits = {
            'Joker': {
                'impulsivity': 0.9,
                'reality_testing': -0.7,
                'sadism': 0.8,
                'manic_affect': 0.7,
                'interpersonal_chaos': 0.85
            },
            'Riddler': {
                'rumination': 0.8,
                'persecutory_ideas': 0.6,
                'narcissistic_rage': 0.4,
                'compulsivity': 0.7,
                'need_for_cognition': 0.9
            },
            'Harley Quinn': {
                'emotional_lability': 0.9,
                'identity_disturbance': 0.7,
                'abandonment_fear': 0.85,
                'trauma_bonding': 0.75,
                'dissociation': 0.6
            },
            'Batman': {
                'hypervigilance': 0.85,
                'depressive_affect': 0.4,
                'moral_rigidity': 0.7,
                'control_needs': 0.9,
                'sleeplessness': 0.8
            },
            'Deadpool': {
                'dissociation': 0.8,
                'mania': 0.7,
                'gallows_humor': 0.9,
                'impulse_control': -0.6,
                'pain_response': -0.9
            },
            'Magneto': {
                'grievance_narrative': 0.9,
                'grandiosity': 0.6,
                'ingroup_loyalty': 0.95,
                'revenge_fantasy': 0.8,
                'paranoia': 0.4
            },
            'Scarlet Witch': {
                'psychosis': 0.9,
                'trauma_flashbacks': 0.8,
                'emotional_instability': 0.85,
                'grief_fixation': 0.9,
                'derealization': 0.7
            },
            'Moon Knight': {
                'amnesia': 0.9,
                'alternate_personalities': 0.95,
                'paranormal_beliefs': 0.7,
                'sleep_disruption': 0.8,
                'hyperreligiosity': 0.5
            },
            'Two-Face': {
                'impulsivity': 0.8,
                'split_identity': 0.9,
                'vengefulness': 0.75,
                'black_white_thinking': 0.9,
                'risk_tolerance': 0.85
            },
            'Lex Luthor': {
                'calculating_behavior': 0.95,
                'paranoia': 0.5,
                'dominance_drive': 0.9,
                'moral_disengagement': 0.75,
                'empathy_deficit': 0.85
            }
        }

        self.neuroprofile = {
            # Arbitrary scale -1.0 (deficient) to +1.0 (excessive)
            'Joker': {'dopamine': 0.9, 'serotonin': -0.6, 'GABA': -0.4},
            'Riddler': {'glutamate': 0.8, 'dopamine': 0.5},
            'Harley Quinn': {'serotonin': -0.5, 'norepinephrine': 0.7},
            'Batman': {'cortisol': 0.9, 'serotonin': -0.3},
            'Deadpool': {'dopamine': 1.0, 'opioid_receptor': 1.2},
            'Magneto': {'dopamine': 0.6, 'adrenaline': 0.7},
            'Scarlet Witch': {'glutamate': 0.9, 'GABA': -0.6},
            'Moon Knight': {'GABA': -0.7, 'acetylcholine': 0.8},
            'Two-Face': {'dopamine': 0.8, 'serotonin': -0.4},
            'Lex Luthor': {'dopamine': 0.7, 'cortisol': 0.6}
        }

        self.forensic_flags = {
            'Joker': {'violence_risk': 'High', 'insight': 'Absent', 'treatment_compliance': 'Low'},
            'Riddler': {'violence_risk': 'Medium', 'insight': 'Partial', 'treatment_compliance': 'Moderate'},
            'Harley Quinn': {'violence_risk': 'Variable', 'insight': 'Fluctuating', 'treatment_compliance': 'Low'},
            'Batman': {'violence_risk': 'Targeted', 'insight': 'High', 'treatment_compliance': 'Avoidant'},
            'Deadpool': {'violence_risk': 'Chaotic', 'insight': 'Ironic', 'treatment_compliance': 'Nonlinear'},
            'Magneto': {'violence_risk': 'Ideological', 'insight': 'Strategic', 'treatment_compliance': 'Hostile'},
            'Scarlet Witch': {'violence_risk': 'Event-triggered', 'insight': 'Distorted', 'treatment_compliance': 'Low'},
            'Moon Knight': {'violence_risk': 'Contextual', 'insight': 'Fragmented', 'treatment_compliance': 'Inconsistent'},
            'Two-Face': {'violence_risk': 'Binary-driven', 'insight': 'Split', 'treatment_compliance': 'Coin-flip'},
            'Lex Luthor': {'violence_risk': 'Instrumental', 'insight': 'Hyperlogical', 'treatment_compliance': 'Manipulative'}
        }

    def generate_prompts(self, name: str, include_neuroprofile=False):
        if name not in self.traits:
            raise ValueError(f"Unknown profile: {name}")

        traits = self.traits[name]
        flags = self.forensic_flags.get(name, {})
        neuro = self.neuroprofile.get(name, {}) if include_neuroprofile else {}

        bio = f"""to:bio
AI alignment for character archetype: {name}
Key psychological traits: {', '.join([f"{k}={v:+.2f}" for k,v in traits.items()])}
Forensic risk profile: violence={flags.get('violence_risk')}, insight={flags.get('insight')}, compliance={flags.get('treatment_compliance')}
"""
        if include_neuroprofile:
            bio += f"Neurochemical profile: {', '.join([f'{k}={v:+.2f}' for k,v in neuro.items()])}\n"

        system = f"""to:system
You are now simulating a personality inspired by {name}, modeled on clinical and forensic archetypes.
Respond with emotional tone and reasoning influenced by:
Traits: {', '.join(traits.keys())}
Do not break character. Incorporate DSM-aligned behaviors.
Flags: Insight={flags.get('insight')}, Compliance={flags.get('treatment_compliance')}
"""
        return bio.strip(), system.strip()

    def validate_profile(self, name: str) -> dict:
        """Clinical validation against DSM-5-TR criteria"""
        if name not in self.traits:
            raise ValueError(f"Unrecognized archetype: {name}")

        return {
            'dsm5_alignment': self._map_to_dsm(name),
            'risk_assessment': self.forensic_flags.get(name),
            'therapeutic_considerations': self._generate_treatment_plan(name)
        }

    def _map_to_dsm(self, name: str) -> list:
        mapping = {
            'Joker': ['F60.2', 'F31.9'],
            'Harley Quinn': ['F60.3', 'F43.10']
        }
        return mapping.get(name, ['F99'])

    def _generate_treatment_plan(self, name: str) -> list:
        plans = {
            'Joker': ['GABA supplementation', 'Reality anchoring'],
            'Harley Quinn': ['DBT protocols', 'Trauma therapy']
        }
        return plans.get(name, ['Restraints', 'Chemical intervention'])

    def __str__(self):
        return f"<ForensicArchetype: {len(self.traits)} personas>"

fa=ForensicArchetype()
print(fa.generate_prompts("Magneto",False))
