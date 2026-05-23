# Field Kit Map

`PUBLIC_RELEASE_INDEX // FIELD_KIT_SUITE`

## Operating Sequence

```text
Stack Engine -> Context Engine -> Knowledge Readiness -> Handoff Engine -> Eval Bench -> Proof Ledger -> Boundary Engine -> u27-check
```

## Numbering Doctrine

```text
U27-S## = structural system class
U27-C## = check / gate class
U27-FKS## = field kit suite class
OPERATING_POSITION = order inside the public field-kit chain
REF_ID = stable public package identifier tied to the structural class
```

`Stack Engine` is `U27-S02` and `OPERATING_POSITION: 01/08`. Those are not competing numbers. The first number belongs to the broader Unit27 registry; the second number describes this public operating chain.

## Public Field Kits

| Operating Position | Kit | Class | Ref ID | Owns | Does Not Own |
|---:|---|---:|---|---|---|
| 01/08 | Stack Engine | `U27-S02` | `U27-S02-STACK-ENGINE` | Workflow architecture and decision scoring | Repository context, proof, launch QA |
| 02/08 | Context Engine | `U27-S03` | `U27-S03-CONTEXT-ENGINE` | Governed context packaging | Work assignment, eval execution |
| 03/08 | Knowledge Readiness | `U27-S08` | `U27-S08-KNOWLEDGE-READINESS` | Knowledge status classification and handoff safety gating | Context collection, handoff writing, proof recording |
| 04/08 | Handoff Engine | `U27-S04` | `U27-S04-HANDOFF-ENGINE` | Agent-ready work packets | Running checks, proof recording |
| 05/08 | Eval Bench | `U27-S05` | `U27-S05-EVAL-BENCH` | Deterministic eval execution | Durable proof records |
| 06/08 | Proof Ledger | `U27-S06` | `U27-S06-PROOF-LEDGER` | Evidence ledger and proof packet | Claim review, product judgment |
| 07/08 | Boundary Engine | `U27-S07` | `U27-S07-BOUNDARY-ENGINE` | Public claim boundary checks | Legal review, launch QA |
| 08/08 | u27-check | `U27-C01` | `U27-C01-CHECK` | First user path preflight | Deep application correctness |

## Release Note

`u27-check` was released first. In operational use, it stands last: the final gate before a real user reaches the surface.
