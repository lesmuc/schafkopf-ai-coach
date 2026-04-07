from typing import TypedDict

class GameState(TypedDict, total=False):
    hand: list[str]
    played_cards: list[str]
    game_type: str
    trump_suit: str
    position: int
    current_trick: list[str]
    valid_moves: list[str]
    move_scores: dict[str, float]
    best_move: str
    explanation: str



    