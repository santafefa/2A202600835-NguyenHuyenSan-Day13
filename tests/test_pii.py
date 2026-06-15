from app.pii import scrub_text


def test_scrub_email() -> None:
    out = scrub_text("Email me at student@vinuni.edu.vn")
    assert "student@" not in out
    assert "REDACTED_EMAIL" in out


def test_scrub_credit_card() -> None:
    out = scrub_text("Here is my credit card 4111-2222-3333-4444 for the payment.")
    assert "4111" not in out
    assert "REDACTED_CREDIT_CARD" in out
