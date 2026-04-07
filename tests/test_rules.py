from app.rules import compute_valid_moves


class TestNoTrickPlayed:
    def test_all_cards_valid_when_no_trick(self):
        state = {
            "hand": ["EO", "GA", "S7"],
            "played_cards": [],
            "game_type": "Sauspiel",
        }
        result = compute_valid_moves(state)
        assert result["valid_moves"] == ["EO", "GA", "S7"]

    def test_all_cards_valid_when_empty_trick(self):
        state = {
            "hand": ["EO", "GA", "S7"],
            "played_cards": [],
            "game_type": "Sauspiel",
            "current_trick": [],
        }
        result = compute_valid_moves(state)
        assert result["valid_moves"] == ["EO", "GA", "S7"]


class TestFarbzwangSauspiel:
    def test_must_play_same_suit(self):
        state = {
            "hand": ["EA", "EK", "GA", "S7"],
            "played_cards": [],
            "game_type": "Sauspiel",
            "current_trick": ["E9"],
        }
        result = compute_valid_moves(state)
        assert result["valid_moves"] == ["EA", "EK"]

    def test_free_if_no_matching_suit(self):
        state = {
            "hand": ["GA", "S7"],
            "played_cards": [],
            "game_type": "Sauspiel",
            "current_trick": ["E9"],
        }
        result = compute_valid_moves(state)
        assert result["valid_moves"] == ["GA", "S7"]

    def test_must_play_trumpf_when_trumpf_led(self):
        state = {
            "hand": ["EO", "HZ", "GA", "S7"],
            "played_cards": [],
            "game_type": "Sauspiel",
            "current_trick": ["HO"],
        }
        result = compute_valid_moves(state)
        # EO und HZ sind Trumpf im Sauspiel (Ober + Herz)
        assert result["valid_moves"] == ["EO", "HZ"]

    def test_unter_is_trumpf_not_suit(self):
        state = {
            "hand": ["EU", "EA", "GA"],
            "played_cards": [],
            "game_type": "Sauspiel",
            "current_trick": ["E9"],
        }
        result = compute_valid_moves(state)
        # EU ist Trumpf, nicht Eichel — nur EA bedient Eichel
        assert result["valid_moves"] == ["EA"]


class TestFarbzwangWenz:
    def test_ober_is_not_trumpf_in_wenz(self):
        state = {
            "hand": ["EO", "EU", "GA"],
            "played_cards": [],
            "game_type": "Wenz",
            "current_trick": ["E9"],
        }
        result = compute_valid_moves(state)
        # Im Wenz ist EO eine normale Eichel-Karte, EU ist Trumpf
        assert result["valid_moves"] == ["EO"]

    def test_unter_is_trumpf_in_wenz(self):
        state = {
            "hand": ["EU", "GU", "EA"],
            "played_cards": [],
            "game_type": "Wenz",
            "current_trick": ["HU"],
        }
        result = compute_valid_moves(state)
        assert result["valid_moves"] == ["EU", "GU"]


class TestFarbzwangFarbSolo:
    def test_trump_suit_cards_are_trumpf(self):
        state = {
            "hand": ["EA", "EK", "GA"],
            "played_cards": [],
            "game_type": "Farb-Solo",
            "trump_suit": "E",
            "current_trick": ["EO"],
        }
        result = compute_valid_moves(state)
        # Alles Eichel + Ober/Unter = Trumpf
        assert result["valid_moves"] == ["EA", "EK"]
