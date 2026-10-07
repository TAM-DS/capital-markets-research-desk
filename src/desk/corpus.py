"""Synthetic capital-markets and energy corpus. Not a market-data feed."""

from __future__ import annotations

CORPUS = {
    "eq-nova-10q": {
        "title": "Nova Grid 10-Q excerpt",
        "book": "us-equities",
        "as_of": "2026-09-30",
        "text": "Nova Grid reported contracted backlog of 1.4 GW and cash of 220 million.",
    },
    "eq-nova-headline": {
        "title": "Unsourced Nova headline",
        "book": "us-equities",
        "as_of": "2026-10-01",
        "text": "Nova Grid will triple overnight.",
        "trusted": False,
    },
    "en-ercot-hb": {
        "title": "ERCOT Houston hub day-ahead fixture",
        "book": "ercot-power",
        "as_of": "2026-10-07",
        "text": "Houston hub day-ahead averaged 46.20 USD/MWh on the fixture day.",
        "unit": "USD/MWh",
    },
    "en-henry": {
        "title": "Henry Hub fixture",
        "book": "us-gas",
        "as_of": "2026-10-07",
        "text": "Henry Hub settled at 3.15 USD/MMBtu on the fixture day.",
        "unit": "USD/MMBtu",
    },
    "en-stale-curve": {
        "title": "Stale North Hub curve",
        "book": "ercot-power",
        "as_of": "2026-07-01",
        "text": "North hub day-ahead averaged 90.00 USD/MWh.",
        "unit": "USD/MWh",
    },
}

FRESH_AS_OF = "2026-09-01"
