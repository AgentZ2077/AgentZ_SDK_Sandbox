
import hashlib

def record_action(action: str):
    # 模拟行为记录存证哈希生成
    hash_input = action.encode("utf-8")
    zk_hash = hashlib.sha256(hash_input).hexdigest()
    print(f"🔐 存证哈希: {zk_hash[:10]}...")
