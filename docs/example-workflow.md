# Example Workflow

`PUBLIC_RELEASE_INDEX // FIELD_KIT_SUITE`

This example shows the public operating sequence. It is intentionally small: one repo, one objective, one chain.

## Scenario

A repository is about to be shared publicly. The owner wants an AI agent to improve the README, but the work needs to stay bounded and the final public claims need proof.

## Sequence

### 1. Shape The Work

Use Stack Engine when the project still needs a decision artifact.

```text
Question: What should be built, delayed, kept manual, or rejected?
Output: Scored workflow architecture and implementation direction.
```

### 2. Package The Context

Use Context Engine when the repository needs governed context before agent work.

```bash
context-engine scan . --max-tokens 50000
```

Output:

```text
context_manifest.md
context_report.json
```

### 3. Write The Handoff

Use Handoff Engine when the agent needs a bounded work packet.

```bash
handoff-engine build \
  --objective "Improve README first-use path" \
  --context context_report.json \
  --allowed README.md \
  --constraint "Keep public claims inside recorded proof." \
  --acceptance "README includes a runnable first-use command." \
  --proof-case readme-first-use-present
```

Output:

```text
u27/handoff.json
u27/HANDOFF_PACKET.md
evals/proof_cases.json
```

### 4. Run The Evals

Use Eval Bench when acceptance checks need executable results.

```bash
eval-bench run
```

Output:

```text
u27/eval_results.json
u27/EVAL_REPORT.md
u27/eval_evidence/*.txt
```

### 5. Record The Proof

Use Proof Ledger when evidence needs to survive the terminal session.

```bash
proof-ledger run --case tests-pass -- python3 -m unittest discover -s tests
proof-ledger packet
```

Output:

```text
u27/proof_ledger.json
u27/PROOF_PACKET.md
u27/evidence/run-0001.txt
```

### 6. Check The Boundary

Use Boundary Engine when public language needs to stay inside recorded proof.

```bash
boundary-engine scan README.md --proof u27/proof_ledger.json
```

Output:

```text
u27/BOUNDARY_REGISTER.md
u27/boundary_report.json
```

### 7. Check The Launch Surface

Use `u27-check` before the demo or launch link is shared.

```bash
u27-check /path/to/project
```

Output:

```text
u27/LAUNCH_PACKET.md
u27/AUDIT_LOG.json
```

## Operating Line

Structure first.
Proof before claim.
Boundaries before scale.
