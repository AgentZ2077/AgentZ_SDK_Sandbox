
# 🧠 AgentZ SDK + Sandbox

A lightweight development toolkit and web sandbox for building, testing and deploying AI agents using the Solana MCP protocol.

---

## 📦 Project Structure

```
AgentZ_SDK_Sandbox/
├── agentz_sdk/           # Core Python SDK
│   ├── core/             # Agent runtime and MCP context tools
│   ├── utils/            # Audit logging
│   └── examples/         # CLI examples for agent behavior
├── sandbox/              # Sandbox environment
│   ├── api/              # FastAPI backend for simulated runtime
│   └── frontend/         # Web UI (HTML prototype)
```

---

## 🧠 Features

- AI Agent runtime orchestration
- MCP context management & toolchain hooks
- CLI-based behavior simulation
- On-chain action logging (ZK-ready)
- FastAPI + HTML sandbox UI (extensible)

---

## 🚀 Getting Started

### Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### Run sandbox locally

```bash
cd sandbox/api
uvicorn main:app --reload
```

Then open your browser at `http://localhost:8000`.

---

## 🧪 Example Usage

```bash
python agentz_sdk/examples/demo_agent.py
```

---

## 🌐 Website

Visit the full project at: [https://agentz2077.org](https://agentz2077.org)

Built with ♥ by AgentZ2077 Core Devs.
