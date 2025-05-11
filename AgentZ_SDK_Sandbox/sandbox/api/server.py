from fastapi import FastAPI, Request
from pydantic import BaseModel
from agentz_sdk.core.context import get_context
from agentz_sdk.utils.skills import SkillExecutor
from agentz_sdk.utils.log import log_action, record_zk_hash

app = FastAPI()

class SkillRequest(BaseModel):
    skill: str

@app.post("/run")
async def run_skill(req: SkillRequest):
    context = get_context()
    executor = SkillExecutor("agentz_sdk/examples/skills.yaml")
    result = executor.execute(req.skill, context)
    log_action(req.skill)
    record_zk_hash(req.skill)
    return {"status": "ok", "skill": req.skill}
