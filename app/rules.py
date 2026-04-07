from app.state import GameState

def compute_valid_moves(state: GameState) -> GameState:
    state["valid_moves"] = state["hand"]
    return state