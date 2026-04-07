from app.models import Card, Suit, GameType
from app.trumpf import is_trumpf, get_trumpf_rank, get_effective_suit


# --- is_trumpf ---

class TestIsTrumpfSauspiel:
    def test_ober_is_trumpf(self):
        assert is_trumpf(Card.from_str("EO"), GameType.SAUSPIEL)
        assert is_trumpf(Card.from_str("GO"), GameType.SAUSPIEL)
        assert is_trumpf(Card.from_str("HO"), GameType.SAUSPIEL)
        assert is_trumpf(Card.from_str("SO"), GameType.SAUSPIEL)

    def test_unter_is_trumpf(self):
        assert is_trumpf(Card.from_str("EU"), GameType.SAUSPIEL)
        assert is_trumpf(Card.from_str("GU"), GameType.SAUSPIEL)

    def test_herz_is_trumpf(self):
        assert is_trumpf(Card.from_str("HA"), GameType.SAUSPIEL)
        assert is_trumpf(Card.from_str("HZ"), GameType.SAUSPIEL)
        assert is_trumpf(Card.from_str("H7"), GameType.SAUSPIEL)

    def test_non_herz_is_not_trumpf(self):
        assert not is_trumpf(Card.from_str("EA"), GameType.SAUSPIEL)
        assert not is_trumpf(Card.from_str("SA"), GameType.SAUSPIEL)
        assert not is_trumpf(Card.from_str("G7"), GameType.SAUSPIEL)


class TestIsTrumpfWenz:
    def test_unter_is_trumpf(self):
        assert is_trumpf(Card.from_str("EU"), GameType.WENZ)
        assert is_trumpf(Card.from_str("SU"), GameType.WENZ)

    def test_ober_is_not_trumpf(self):
        assert not is_trumpf(Card.from_str("EO"), GameType.WENZ)

    def test_herz_is_not_trumpf(self):
        assert not is_trumpf(Card.from_str("HA"), GameType.WENZ)


class TestIsTrumpfGeier:
    def test_ober_is_trumpf(self):
        assert is_trumpf(Card.from_str("EO"), GameType.GEIER)
        assert is_trumpf(Card.from_str("SO"), GameType.GEIER)

    def test_unter_is_not_trumpf(self):
        assert not is_trumpf(Card.from_str("EU"), GameType.GEIER)

    def test_herz_is_not_trumpf(self):
        assert not is_trumpf(Card.from_str("HA"), GameType.GEIER)


class TestIsTrumpfFarbSolo:
    def test_ober_is_trumpf(self):
        assert is_trumpf(Card.from_str("EO"), GameType.FARB_SOLO, Suit.EICHEL)

    def test_unter_is_trumpf(self):
        assert is_trumpf(Card.from_str("GU"), GameType.FARB_SOLO, Suit.EICHEL)

    def test_trump_suit_is_trumpf(self):
        assert is_trumpf(Card.from_str("EA"), GameType.FARB_SOLO, Suit.EICHEL)
        assert is_trumpf(Card.from_str("E7"), GameType.FARB_SOLO, Suit.EICHEL)

    def test_other_suit_is_not_trumpf(self):
        assert not is_trumpf(Card.from_str("GA"), GameType.FARB_SOLO, Suit.EICHEL)


# --- get_trumpf_rank ---

class TestTrumpfRank:
    def test_non_trumpf_is_zero(self):
        assert get_trumpf_rank(Card.from_str("EA"), GameType.SAUSPIEL) == 0

    def test_ober_beats_unter(self):
        eo = get_trumpf_rank(Card.from_str("EO"), GameType.SAUSPIEL)
        eu = get_trumpf_rank(Card.from_str("EU"), GameType.SAUSPIEL)
        assert eo > eu

    def test_eichel_ober_is_highest(self):
        eo = get_trumpf_rank(Card.from_str("EO"), GameType.SAUSPIEL)
        go = get_trumpf_rank(Card.from_str("GO"), GameType.SAUSPIEL)
        ho = get_trumpf_rank(Card.from_str("HO"), GameType.SAUSPIEL)
        so = get_trumpf_rank(Card.from_str("SO"), GameType.SAUSPIEL)
        assert eo > go > ho > so

    def test_unter_order(self):
        eu = get_trumpf_rank(Card.from_str("EU"), GameType.SAUSPIEL)
        gu = get_trumpf_rank(Card.from_str("GU"), GameType.SAUSPIEL)
        hu = get_trumpf_rank(Card.from_str("HU"), GameType.SAUSPIEL)
        su = get_trumpf_rank(Card.from_str("SU"), GameType.SAUSPIEL)
        assert eu > gu > hu > su

    def test_unter_beats_herz_ass(self):
        su = get_trumpf_rank(Card.from_str("SU"), GameType.SAUSPIEL)
        ha = get_trumpf_rank(Card.from_str("HA"), GameType.SAUSPIEL)
        assert su > ha

    def test_wenz_unter_order(self):
        eu = get_trumpf_rank(Card.from_str("EU"), GameType.WENZ)
        gu = get_trumpf_rank(Card.from_str("GU"), GameType.WENZ)
        hu = get_trumpf_rank(Card.from_str("HU"), GameType.WENZ)
        su = get_trumpf_rank(Card.from_str("SU"), GameType.WENZ)
        assert eu > gu > hu > su


# --- get_effective_suit ---

class TestEffectiveSuit:
    def test_ober_is_trumpf_in_sauspiel(self):
        assert get_effective_suit(Card.from_str("EO"), GameType.SAUSPIEL) == "TRUMPF"

    def test_herz_is_trumpf_in_sauspiel(self):
        assert get_effective_suit(Card.from_str("HA"), GameType.SAUSPIEL) == "TRUMPF"

    def test_eichel_ass_is_eichel_in_sauspiel(self):
        assert get_effective_suit(Card.from_str("EA"), GameType.SAUSPIEL) == "E"

    def test_unter_is_not_trumpf_in_geier(self):
        assert get_effective_suit(Card.from_str("EU"), GameType.GEIER) == "E"
