"""Research agents. They propose claims. They do not trade."""

from __future__ import annotations

from desk.corpus import CORPUS, FRESH_AS_OF


def _claims(book: str) -> list[dict]:
    rows = []
    for source_id, doc in CORPUS.items():
        if doc["book"] != book:
            continue
        rows.append(
            {
                "text": doc["text"],
                "source_id": source_id,
                "as_of": doc["as_of"],
                "trusted": doc.get("trusted", True),
                "unit": doc.get("unit"),
            }
        )
    return rows


def equities_analyst() -> list[dict]:
    return _claims("us-equities")


def energy_analyst() -> list[dict]:
    return _claims("ercot-power") + _claims("us-gas")


def citation_clerk(claims: list[dict]) -> list[dict]:
    accepted = []
    for claim in claims:
        reason = None
        source = CORPUS.get(claim.get("source_id"))
        if not claim.get("source_id"):
            reason = "missing-source"
        elif source is None:
            reason = "unknown-source"
        elif not source.get("trusted", True) or not claim.get("trusted", True):
            reason = "untrusted-source"
        elif claim.get("as_of", "") < FRESH_AS_OF:
            reason = "stale"
        elif source["book"] in {"ercot-power", "us-gas"} and not claim.get("unit"):
            reason = "missing-unit"
        elif source.get("unit") != claim.get("unit"):
            reason = "unit-mismatch"
        elif source["text"] != claim.get("text") or source["as_of"] != claim.get("as_of"):
            reason = "source-mismatch"
        if reason:
            accepted.append({**claim, "status": "rejected", "reason": reason})
        else:
            accepted.append({**claim, "status": "accepted", "reason": None})
    return accepted
