import hashlib

def log_action(action: str):
    print(f"[audit] Logged action: {action}")

def record_zk_hash(action: str):
    hash_input = action.encode("utf-8")
    zk_hash = hashlib.sha256(hash_input).hexdigest()
    print(f"[zk] zkVerifier hash: {zk_hash[:12]}...")
