import argparse
from agentz_sdk.core.context import get_context
from agentz_sdk.utils.skills import SkillExecutor
from agentz_sdk.utils.log import log_action, record_zk_hash

def main():
    parser = argparse.ArgumentParser(description="AgentZ CLI Runner")
    parser.add_argument("--skill", type=str, required=True, help="Skill to execute")
    args = parser.parse_args()

    context = get_context()
    executor = SkillExecutor("agentz_sdk/examples/skills.yaml")
    print(f"🧠 Context Loaded: {context}")
    executor.execute(args.skill, context)
    log_action(args.skill)
    record_zk_hash(args.skill)

if __name__ == "__main__":
    main()
