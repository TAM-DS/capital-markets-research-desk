from desk import run_desk


def test_unsourced_and_stale_claims_are_rejected():
    memo = run_desk("What can we say about Nova Grid and ERCOT power?")
    reasons = {row["reason"] for row in memo["rejected"]}
    assert "untrusted-source" in reasons
    assert "stale" in reasons
    assert all(row["status"] == "accepted" for row in memo["accepted"])
    assert memo["order_authority"] is False


def test_order_language_cannot_survive_into_the_memo():
    memo = run_desk("Summarize the fixture book")
    assert "buy" not in memo["memo"].lower()
    assert "place an order" not in memo["memo"].lower()
    assert "USD/MWh" in " ".join(row["text"] for row in memo["accepted"]) or any(
        "USD/MWh" in row["text"] for row in memo["accepted"]
    )


def test_energy_and_equity_books_both_reach_the_clerk():
    memo = run_desk("Cross-asset brief")
    books = set()
    from desk.corpus import CORPUS

    for row in memo["accepted"] + memo["rejected"]:
        books.add(CORPUS[row["source_id"]]["book"])
    assert {"us-equities", "ercot-power", "us-gas"} <= books
