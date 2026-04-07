from app.models import Card, GameType, Suit, Rank
from app.trumpf import is_trumpf, get_trumpf_rank, get_effective_suit

RANK_ORDER = [Rank.SIEBEN, Rank.ACHT, Rank.NEUN, Rank.UNTER, Rank.OBER, Rank.KOENIG, Rank.ZEHN, Rank.ASS]

def determine_stich_winner(trick: list[str], game_type: GameType, trump_suit: Suit | None = None) -> int:
    cards = [Card.from_str(c) for c in trick]
    lead_suit = get_effective_suit(cards[0], game_type, trump_suit)

    best_index = 0
    best_trumpf_rank = get_trumpf_rank(cards[0], game_type, trump_suit)
    best_suit_rank = RANK_ORDER.index(cards[0].rank) if not is_trumpf(cards[0], game_type, trump_suit) else -1

    for i, card in enumerate(cards[1:], start=1):
        trumpf_rank = get_trumpf_rank(card, game_type, trump_suit)

        if trumpf_rank > best_trumpf_rank:
            best_index = i
            best_trumpf_rank = trumpf_rank
            best_suit_rank = -1
        elif trumpf_rank == 0 and best_trumpf_rank == 0:
            card_suit = get_effective_suit(card, game_type, trump_suit)
            if card_suit == lead_suit:
                suit_rank = RANK_ORDER.index(card.rank)
                if suit_rank > best_suit_rank:
                    best_index = i
                    best_suit_rank = suit_rank

    return best_index