"""Verify the public Unit27 Field Kit Suite documentation contract."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "docs/example-workflow.md",
    "docs/field-kit-map.md",
]
REQUIRED_TERMS = [
    "unit27-stack-engine",
    "unit27-context-engine",
    "unit27-handoff-engine",
    "unit27-eval-bench",
    "unit27-proof-ledger",
    "unit27-boundary-engine",
    "u27-check",
    "U27-FKS01",
    "U27-S02-STACK-ENGINE",
    "OPERATING_POSITION",
    "Numbering Doctrine",
    "Stack Engine -> Context Engine -> Handoff Engine -> Eval Bench -> Proof Ledger -> Boundary Engine -> u27-check",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        print("missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing_terms = [term for term in REQUIRED_TERMS if term not in readme]
    if missing_terms:
        print("missing required README terms:")
        for term in missing_terms:
            print(f"- {term}")
        return 1

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "MIT License" not in license_text or "Unit27 Research" not in license_text:
        print("license is not the expected Unit27 Research MIT license")
        return 1

    print("suite documentation verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
