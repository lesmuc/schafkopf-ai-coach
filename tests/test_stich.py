from app.models import GameType, Suit
from app.stich import determine_stich_winner


class TestStichSauspiel:
    def test_highest_trumpf_wins(self):
        # EO (höchster Trumpf) gewinnt
        trick = ["GO", "EO", "HU", "SU"]
        assert determine_stich_winner(trick, GameType.SAUSPIEL) == 1

    def test_trumpf_beats_non_trumpf(self):
        # H7 ist Trumpf im Sauspiel, schlägt Eichel-Ass
        trick = ["EA", "H7", "E9", "EK"]
        assert determine_stich_winner(trick, GameType.SAUSPIEL) == 1

    def test_highest_suit_card_wins_without_trumpf(self):
        # Kein Trumpf gespielt, EA ist höchste Eichel
        trick = ["E9", "EA", "EK", "E8"]
        assert determine_stich_winner(trick, GameType.SAUSPIEL) == 1

    def test_first_player_wins_on_tie_suit(self):
        # Erster Spieler hat angespielt, niemand überbietet
        trick = ["EA", "G7", "S9", "SK"]
        assert determine_stich_winner(trick, GameType.SAUSPIEL) == 0

    def test_off_suit_cannot_win(self):
        # Gras-Ass kann Eichel-Stich nicht gewinnen (kein Trumpf)
        trick = ["EK", "GA", "E8", "E9"]
        assert determine_stich_winner(trick, GameType.SAUSPIEL) == 0


class TestStichWenz:
    def test_unter_wins(self):
        trick = ["EA", "EU", "GA", "SA"]
        assert determine_stich_winner(trick, GameType.WENZ) == 1

    def test_higher_unter_wins(self):
        trick = ["SU", "HU", "GU", "EU"]
        assert determine_stich_winner(trick, GameType.WENZ) == 3

    def test_ober_is_normal_card_in_wenz(self):
        # EO ist nur eine Eichel-Karte, keine Trumpf
        trick = ["EA", "EO", "EK", "EZ"]
        # EA > EO? Nein — Rang-Reihenfolge: Ass > Zehn > König > ... > Ober
        # Aber EO ist kein Standard-Rang in RANK_ORDER...
        # Im Wenz zählt Ober als normale Farbkarte
        assert determine_stich_winner(trick, GameType.WENZ) == 0


class TestStichFarbSolo:
    def test_trump_suit_wins(self):
        trick = ["GA", "EA", "SA", "HA"]
        assert determine_stich_winner(trick, GameType.FARB_SOLO, Suit.EICHEL) == 1
