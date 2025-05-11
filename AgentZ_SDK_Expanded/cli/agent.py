
from mcp.context import get_context
from verifier.log import record_action

def run_agent():
    print("🚀 AgentZ CLI 启动中...")
    context = get_context()
    print(f"📥 获取上下文: {context}")
    
    decision = "mint_elven_wine"
    print(f"🧠 Agent 推理输出: {decision}")
    
    record_action(decision)
    print("✅ 行为已模拟执行并存证")
    
if __name__ == "__main__":
    run_agent()
