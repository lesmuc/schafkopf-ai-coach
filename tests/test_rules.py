from app.rules import compute_valid_moves

def test_all_hands_are_valid_moves():
    state = {
        "hand": ["HO", "SU", "GA"],
        "played_cards": [],
        "game_type": "Sauspiel"
    }
    result = compute_valid_moves(state)
    assert result["valid_moves"] == ["HO", "SU", "GA"]