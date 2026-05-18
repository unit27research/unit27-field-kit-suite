# Field Kit Map

`PUBLIC_RELEASE_INDEX // FIELD_KIT_SUITE`

## Operating Sequence

```text
Stack Engine -> Context Engine -> Handoff Engine -> Eval Bench -> Proof Ledger -> Boundary Engine -> u27-check
```

## Numbering Doctrine

```text
U27-S## = structural system class
U27-C## = check / gate class
U27-FKS## = field kit suite class
OPERATING_POSITION = order inside the public field-kit chain
REF_ID = stable public package identifier tied to the structural class
```

`Stack Engine` is `U27-S02` and `OPERATING_POSITION: 01/07`. Those are not competing numbers. The first number belongs to the broader Unit27 registry; the second number describes this public operating chain.

## Public Field Kits

| Operating Position | Kit | Class | Ref ID | Owns | Does Not Own |
|---:|---|---:|---|---|---|
| 01/07 | Stack Engine | `U27-S02` | `U27-S02-STACK-ENGINE` | Workflow architecture and decision scoring | Repository context, proof, launch QA |
| 02/07 | Context Engine | `U27-S03` | `U27-S03-CONTEXT-ENGINE` | Governed context packaging | Work assignment, eval execution |
| 03/07 | Handoff Engine | `U27-S04` | `U27-S04-HANDOFF-ENGINE` | Agent-ready work packets | Running checks, proof recording |
| 04/07 | Eval Bench | `U27-S05` | `U27-S05-EVAL-BENCH` | Deterministic eval execution | Durable proof records |
| 05/07 | Proof Ledger | `U27-S06` | `U27-S06-PROOF-LEDGER` | Evidence ledger and proof packet | Claim review, product judgment |
| 06/07 | Boundary Engine | `U27-S07` | `U27-S07-BOUNDARY-ENGINE` | Public claim boundary checks | Legal review, launch QA |
| 07/07 | u27-check | `U27-C01` | `U27-C01-CHECK` | First user path preflight | Deep application correctness |

## Release Note

`u27-check` was released first. In operational use, it stands last: the final gate before a real user reaches the surface.
