# Unit27 Field Kit Suite

[![CI](https://github.com/unit27research/unit27-field-kit-suite/actions/workflows/ci.yml/badge.svg)](https://github.com/unit27research/unit27-field-kit-suite/actions/workflows/ci.yml)

`PUBLIC_RELEASE_INDEX // FIELD_KIT_SUITE`

Unit27 Field Kit Suite is the public binder for the Unit27 open tooling channel.

It does not replace the field kits. It shows how to use them together.

```text
FIELD KIT SUITE

CLASS: SUITE
FUNCTION: Public Orientation + Operating Sequence Guide
REF_ID: FIELD-KIT-SUITE-01
```

## Release Status

`SOURCE_STATUS: PUBLIC_PACKAGE`
`ACCESS_STATUS: CLEARED_FOR_EXTERNAL_USE`

This repository is a released Unit27 orientation package: visible, inspectable, and intended for practical use. Controlled protocol materials remain outside this source package.

It answers one narrow question:

> How do the Unit27 public field kits fit together, and where should a new user start?

## Start Here

Use the operating sequence, not the release dates:

```text
Stack Engine -> Context Engine -> Handoff Engine -> Eval Bench -> Proof Ledger -> Boundary Engine -> u27-check
```

The short version:

1. Shape the work.
2. Package the context.
3. Write the handoff.
4. Run the evals.
5. Record the proof.
6. Contain the public claim.
7. Check the launch surface.

## Clone The Suite

The current public packages are GitHub-first. Clone the repos and install each field kit from its own README.

```bash
git clone https://github.com/unit27research/unit27-stack-engine
git clone https://github.com/unit27research/unit27-context-engine
git clone https://github.com/unit27research/unit27-handoff-engine
git clone https://github.com/unit27research/unit27-eval-bench
git clone https://github.com/unit27research/unit27-proof-ledger
git clone https://github.com/unit27research/unit27-boundary-engine
git clone https://github.com/unit27research/u27-check
```

## Field Kits

| Repository | System Class | Role |
|---|---:|---|
| [`unit27-stack-engine`](https://github.com/unit27research/unit27-stack-engine) | `U27-S02` | Turns ambiguous operational goals into scored AI workflow architectures. |
| [`unit27-context-engine`](https://github.com/unit27research/unit27-context-engine) | `U27-S03` | Converts repositories into governed, token-aware context packages. |
| [`unit27-handoff-engine`](https://github.com/unit27research/unit27-handoff-engine) | `U27-S04` | Converts objectives and context into agent-ready work packets. |
| [`unit27-eval-bench`](https://github.com/unit27research/unit27-eval-bench) | `U27-S05` | Runs deterministic eval cases before proof recording. |
| [`unit27-proof-ledger`](https://github.com/unit27research/unit27-proof-ledger) | `U27-S06` | Records durable proof artifacts from evals, demos, and test runs. |
| [`unit27-boundary-engine`](https://github.com/unit27research/unit27-boundary-engine) | `U27-S07` | Checks public claims against recorded proof. |
| [`u27-check`](https://github.com/unit27research/u27-check) | `U27-C01` | Runs deterministic pre-launch checks against the first user path. |

## First Use Path

Start with one project and move only as far as the work needs.

```text
1. If the project shape is unclear, use Stack Engine.
2. If repository context is too loose, use Context Engine.
3. If an agent needs bounded work, use Handoff Engine.
4. If checks need executable results, use Eval Bench.
5. If evidence needs to survive, use Proof Ledger.
6. If public claims need discipline, use Boundary Engine.
7. If a demo or launch surface is about to be shared, use u27-check.
```

## Example Workflow

See [docs/example-workflow.md](docs/example-workflow.md) for a complete public-chain example.

## What This Is Not

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
