from pathlib import Path

vault = Path("vault")

# === FILES TO ADD ===

files_to_create = {
    # Meta Doctrine
    vault
    / "meta"
    / "doctrine"
    / "security_design.md": """# Security by Design

A working philosophy of systems that secure themselves — through architecture, not patchwork.

## Principles
- Signal fidelity over volume
- Identity as perimeter
- Context-aware enforcement
- Observability built-in, not bolted-on

> "A breach is often a design flaw that passed audit."
""",
    vault
    / "meta"
    / "doctrine"
    / "operational_philosophy.md": """# Operational Philosophy

## Quiet Wins
Security maturity isn't loud — it's present in fewer alerts, calmer escalations, and predictable recoveries.

## Priorities
- Policies that reduce toil
- Threat intel integrated into feedback loops
- Systems that learn and adapt

""",
    # Personal Signal Mapping
    vault
    / "growth"
    / "ciso_map.md": """# CISO Map

## Trajectory

- Infra-first security, built into deployment paths
- Detection logic as code
- Maturity through architecture, not appearances

## Signals to Amplify
- Thoughtful risk management
- Systemic thinking
- Influence without needing noise

""",
    # Maturity Model
    vault
    / "knowledge"
    / "maturity_model_v1.md": """# Security Capability Maturity Model v1

| Level | Capability Description |
|-------|------------------------|
| 0 | Ad hoc / undefined security controls |
| 1 | Basic policy enforcement |
| 2 | Reactive controls with visibility |
| 3 | Proactive control automation |
| 4 | Adaptive + learning system with governance feedback |

> Customize for Cloud, Infra, AppSec, GRC layers.

""",
    # Evaluator project starter
    vault
    / "projects"
    / "evaluator"
    / "README.md": """# Evaluator

### Mission:
A system that **evaluates before it alerts**, reducing false positives and enforcing policy-as-code at the edge.

## Modules to build:
- Subscription management
- Trigger logic with throttling
- Policy evaluation engine
- Notification router

""",
    vault
    / "projects"
    / "evaluator"
    / "main.py": """# Entry point for Evaluator System

def evaluate_event(event):
    # Placeholder for event evaluation logic
    return "pass"

if __name__ == "__main__":
    sample = {"event_type": "api_call", "source": "svc-auth"}
    print("Eval Result:", evaluate_event(sample))
""",
}

# === EXECUTE CREATION ===

for path, content in files_to_create.items():
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content)
            print(f"✅ Created: {path}")
        else:
            print(f"⚠️ Already exists: {path}")
    except Exception as e:
        print(f"❌ Error creating {path}: {e}")
