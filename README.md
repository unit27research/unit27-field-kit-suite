# U27-FKS01 // Field Kit Suite

[![CI](https://github.com/unit27research/unit27-field-kit-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/unit27research/unit27-field-kit-suite/actions/workflows/ci.yml)

`PUBLIC_RELEASE_INDEX // FIELD_KIT_SUITE`

Unit27 Field Kit Suite orients users to the Unit27 open tooling channel.

It does not replace the field kits. It shows how to use them together.

```text
U27-FKS01
UNIT27 FIELD KIT SUITE

CLASS: SUITE
OPERATING_POSITION: INDEX
FUNCTION: Public Orientation + Operating Sequence Guide
REF_ID: U27-FKS01-FIELD-KIT-SUITE
```

## Release Status

`SOURCE_STATUS: PUBLIC_PACKAGE`
`ACCESS_STATUS: CLEARED_FOR_EXTERNAL_USE`

This repository is a released Unit27 field kit suite: visible, inspectable, and intended for orientation, testing, and practical use. Controlled protocol materials remain outside this source package.

It answers one narrow question:

> How do the Unit27 public field kits fit together, and where should a new user start?

## Start Here

Use the operating sequence, not the release dates:

```text
Stack Engine -> Context Engine -> Knowledge Readiness -> Handoff Engine -> Eval Bench -> Proof Ledger -> Boundary Engine -> u27-check
```

The short version:

1. Shape the work.
2. Package the context.
3. Classify what the context is allowed to become.
4. Write the handoff.
5. Run the evals.
6. Record the proof.
7. Contain the public claim.
8. Check the launch surface.

## Clone The Field Kits

The current public packages are GitHub-first. Clone the repos and install each field kit from its own README.

```bash
git clone https://github.com/unit27research/unit27-stack-engine
git clone https://github.com/unit27research/unit27-context-engine
git clone https://github.com/unit27research/unit27-knowledge-readiness
git clone https://github.com/unit27research/unit27-handoff-engine
git clone https://github.com/unit27research/unit27-eval-bench
git clone https://github.com/unit27research/unit27-proof-ledger
git clone https://github.com/unit27research/unit27-boundary-engine
git clone https://github.com/unit27research/u27-check
```

## Field Kits

| Repository | System Class | Operating Position | Ref ID | Role |
|---|---:|---:|---|---|
| [`unit27-stack-engine`](https://github.com/unit27research/unit27-stack-engine) | `U27-S02` | `01/08` | `U27-S02-STACK-ENGINE` | Turns ambiguous operational goals into scored AI workflow architectures. |
| [`unit27-context-engine`](https://github.com/unit27research/unit27-context-engine) | `U27-S03` | `02/08` | `U27-S03-CONTEXT-ENGINE` | Converts repositories into governed, token-aware context packages. |
| [`unit27-knowledge-readiness`](https://github.com/unit27research/unit27-knowledge-readiness) | `U27-S08` | `03/08` | `U27-S08-KNOWLEDGE-READINESS` | Classifies internal knowledge before it becomes memory, onboarding, automation context, handoff material, or public proof. |
| [`unit27-handoff-engine`](https://github.com/unit27research/unit27-handoff-engine) | `U27-S04` | `04/08` | `U27-S04-HANDOFF-ENGINE` | Converts objectives and approved context into agent-ready work packets. |
| [`unit27-eval-bench`](https://github.com/unit27research/unit27-eval-bench) | `U27-S05` | `05/08` | `U27-S05-EVAL-BENCH` | Runs deterministic eval cases before proof recording. |
| [`unit27-proof-ledger`](https://github.com/unit27research/unit27-proof-ledger) | `U27-S06` | `06/08` | `U27-S06-PROOF-LEDGER` | Records durable proof artifacts from evals, demos, and test runs. |
| [`unit27-boundary-engine`](https://github.com/unit27research/unit27-boundary-engine) | `U27-S07` | `07/08` | `U27-S07-BOUNDARY-ENGINE` | Checks public claims against recorded proof. |
| [`u27-check`](https://github.com/unit27research/u27-check) | `U27-C01` | `08/08` | `U27-C01-CHECK` | Runs deterministic pre-launch checks against the first user path. |

## Numbering Doctrine

Unit27 uses structural class numbers and operating positions separately.

```text
U27-S## = structural system class
U27-C## = check / gate class
U27-FKS## = field kit suite class
OPERATING_POSITION = order inside the public field-kit chain
REF_ID = stable public package identifier tied to the structural class
```

That distinction is intentional. `Stack Engine` is `U27-S02` because the class belongs to the broader Unit27 system registry. It is still `OPERATING_POSITION: 01/08` inside the public field-kit chain.

## First Use Path

Start with one project and move only as far as the work needs.

```text
1. If the project shape is unclear, use Stack Engine.
2. If repository context is too loose, use Context Engine.
3. If prepared context may be stale, disputed, restricted, role-specific, or unsafe for action, use Knowledge Readiness.
4. If an agent needs bounded work, use Handoff Engine.
5. If checks need executable results, use Eval Bench.
6. If evidence needs to survive, use Proof Ledger.
7. If public claims need discipline, use Boundary Engine.
8. If a demo or launch surface is about to be shared, use u27-check.
```

## Example Workflow

See [docs/example-workflow.md](docs/example-workflow.md) for a complete public-chain example.

## What It Does Not Do

Field Kit Suite does not:

1. Bundle the tools into one package manager release
2. Replace each field kit's README
3. Hide the boundaries between the tools
4. Claim the system is complete for every project
5. Publish controlled Unit27 protocol materials

## Verify

```bash
python3 scripts/verify_suite.py
```

## License

MIT
