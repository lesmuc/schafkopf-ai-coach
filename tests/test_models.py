from app.models import Card, Suit, Rank


def test_card_from_str():
    card = Card.from_str("EO")
    assert card.suit == Suit.EICHEL
    assert card.rank == Rank.OBER


def test_card_repr():
    card = Card(Suit.HERZ, Rank.SIEBEN)
    assert repr(card) == "H7"


def test_card_equality():
    assert Card.from_str("EO") == Card.from_str("EO")
    assert Card.from_str("EO") != Card.from_str("GU")


def test_card_from_str_all_suits():
    assert Card.from_str("EO").suit == Suit.EICHEL
    assert Card.from_str("GO").suit == Suit.GRAS
    assert Card.from_str("HO").suit == Suit.HERZ
    assert Card.from_str("SO").suit == Suit.SCHELLEN


def test_card_from_str_all_ranks():
    assert Card.from_str("EO").rank == Rank.OBER
    assert Card.from_str("EU").rank == Rank.UNTER
    assert Card.from_str("EA").rank == Rank.ASS
    assert Card.from_str("EZ").rank == Rank.ZEHN
    assert Card.from_str("EK").rank == Rank.KOENIG
    assert Card.from_str("E9").rank == Rank.NEUN
    assert Card.from_str("E8").rank == Rank.ACHT
    assert Card.from_str("E7").rank == Rank.SIEBEN
