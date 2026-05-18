# Field Kit Map

`PUBLIC_RELEASE_INDEX // FIELD_KIT_SUITE`

## Operating Sequence

```text
Stack Engine -> Context Engine -> Handoff Engine -> Eval Bench -> Proof Ledger -> Boundary Engine -> u27-check
```

## Public Field Kits

| Order | Kit | Class | Owns | Does Not Own |
|---:|---|---:|---|---|
| 1 | Stack Engine | `U27-S02` | Workflow architecture and decision scoring | Repository context, proof, launch QA |
| 2 | Context Engine | `U27-S03` | Governed context packaging | Work assignment, eval execution |
| 3 | Handoff Engine | `U27-S04` | Agent-ready work packets | Running checks, proof recording |
| 4 | Eval Bench | `U27-S05` | Deterministic eval execution | Durable proof records |
| 5 | Proof Ledger | `U27-S06` | Evidence ledger and proof packet | Claim review, product judgment |
| 6 | Boundary Engine | `U27-S07` | Public claim boundary checks | Legal review, launch QA |
| 7 | u27-check | `U27-C01` | First user path preflight | Deep application correctness |

## Release Note

`u27-check` was released first. In operational use, it stands last: the final gate before a real user reaches the surface.
