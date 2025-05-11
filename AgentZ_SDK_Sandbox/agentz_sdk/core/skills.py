
# agentz_sdk/core/skills.py

SKILLS_REGISTRY = {
    "mint_elven_wine": {
        "description": "Mint an Elven Wine NFT",
        "required_context": ["inventory", "quest_state"],
        "exec": lambda ctx: f"Minting elven wine for {ctx['player_id']}"
    },
    "greet_hero": {
        "description": "Greet a visiting hero",
        "required_context": ["reputation"],
        "exec": lambda ctx: f"Welcome, hero with reputation {ctx['reputation']}!"
    }
}

def list_skills():
    return list(SKILLS_REGISTRY.keys())

def execute_skill(skill_name, context):
    if skill_name not in SKILLS_REGISTRY:
        raise ValueError(f"Unknown skill: {skill_name}")
    skill = SKILLS_REGISTRY[skill_name]
    return skill["exec"](context)
