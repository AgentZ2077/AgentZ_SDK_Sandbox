from agentz_sdk.core.context import get_context
from agentz_sdk.utils.skills import SkillExecutor
from agentz_sdk.utils.log import log_action, record_zk_hash

def test_skill_flow():
    context = get_context()
    executor = SkillExecutor("agentz_sdk/examples/skills.yaml")
    skills = executor.list_skills()
    assert "mint_elven_wine" in skills
    success = executor.execute("mint_elven_wine", context)
    assert success
    log_action("mint_elven_wine")
    record_zk_hash("mint_elven_wine")
