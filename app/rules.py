from app.state import GameState
from app.models import Card, GameType, Suit
from app.trumpf import get_effective_suit

def compute_valid_moves(state: GameState) -> GameState:
    hand = [Card.from_str(c) for c in state["hand"]]
    game_type = GameType(state["game_type"])
    trump_suit = Suit(state["trump_suit"]) if state.get("trump_suit") else None
    current_trick = state.get("current_trick", [])

    # Noch kein Stich, dann kann jede Karte gespielt werden
    if not current_trick:
        state["valid_moves"] = state["hand"]
        return state
    
    lead_card = Card.from_str(current_trick[0])
    lead_suit = get_effective_suit(lead_card, game_type, trump_suit)

    matching = [c for c in hand if get_effective_suit(c, game_type, trump_suit) == lead_suit]

    if matching:
        state["valid_moves"] = [repr(c) for c in matching]
    else:
        state["valid_moves"] = state["hand"]

    return state