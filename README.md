# Capital-markets research desk

A team of agents drafts a capital-markets and energy brief. A citation clerk accepts or rejects each claim. The desk cannot place an order.

This is the research seat for the paper trading floor. A memo from this desk is an input, not a ticket.

## What it does

- An equities analyst reads a synthetic filing excerpt.
- An energy analyst reads an ERCOT hub fixture and a Henry Hub fixture, with units.
- A citation clerk rejects an untrusted source and a stale curve.
- The coordinator strips order language from the memo.

## What it does not do

- It does not call a model provider. The agents are deterministic so the tests are the evidence.
- It does not retrieve live filings, live ERCOT prices, or a broker.
- An accepted claim is not a price target and not a recommendation to trade.

## Run

```bash
python -m pytest
```

Related: [investment-gems](https://github.com/TAM-DS/investment-gems) is suggestion-only. [paper-trading-floor](https://github.com/TAM-DS/paper-trading-floor) is the only place a paper fill can exist.
