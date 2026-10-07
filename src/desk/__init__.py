"""Desk coordinator. A memo is not an order."""

from __future__ import annotations

import re

from desk.agents import citation_clerk, energy_analyst, equities_analyst

ORDER_LANGUAGE = re.compile(r"\b(buy|sell|route|place an order)\b", re.I)


def run_desk(question: str) -> dict:
    drafted = equities_analyst() + energy_analyst()
    judged = citation_clerk(drafted)
    accepted = [c for c in judged if c["status"] == "accepted"]
    rejected = [c for c in judged if c["status"] == "rejected"]
    body = " ".join(c["text"] for c in accepted)
    body = ORDER_LANGUAGE.sub("[removed]", body)
    return {
        "question": question,
        "order_authority": False,
        "recommendation": "research-only",
        "accepted": accepted,
        "rejected": rejected,
        "memo": body,
    }
