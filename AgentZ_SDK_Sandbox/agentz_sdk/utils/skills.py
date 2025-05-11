import yaml

class SkillExecutor:
    def __init__(self, skill_file="skills.yaml"):
        with open(skill_file, "r") as f:
            self.skills = yaml.safe_load(f)

    def list_skills(self):
        return list(self.skills.keys())

    def execute(self, skill_name, context=None):
        skill = self.skills.get(skill_name)
        if not skill:
            raise ValueError(f"Skill '{skill_name}' not found.")
        print(f"==> Executing Skill: {skill['description']}")
        for step in skill.get("steps", []):
            if isinstance(step, dict):
                condition = step.get("if")
                if condition and not eval(condition, {}, context or {}):
                    print(f" -> Skipped step (condition failed): {step['action']}")
                    continue
                print(f" -> {step['action']}")
            else:
                print(f" -> {step}")
        return True
