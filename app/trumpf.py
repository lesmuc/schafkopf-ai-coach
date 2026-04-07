from app.models import Card, Suit, Rank, GameType

SUIT_ORDER = [Suit.EICHEL, Suit.GRAS, Suit.HERZ, Suit.SCHELLEN]
RANK_ORDER = [Rank.ASS, Rank.ZEHN, Rank.KOENIG, Rank.NEUN, Rank.ACHT, Rank.SIEBEN]

def is_trumpf(card: Card, game_type: GameType, trump_suit: Suit | None = None) -> bool:
    if game_type == GameType.WENZ:
        return card.rank == Rank.UNTER
    if game_type == GameType.GEIER:
        return card.rank == Rank.OBER
    # Sauspiel oder Farb-Solo
    if card.rank in (Rank.OBER, Rank.UNTER):
        return True
    farbe = trump_suit if game_type == GameType.FARB_SOLO else Suit.HERZ
    return card.suit == farbe

def get_trumpf_rank(card: Card, game_type: GameType, trump_suit: Suit | None = None) -> int:
    if not is_trumpf(card, game_type, trump_suit):
        return 0
    
    if game_type == GameType.WENZ:
        return len(SUIT_ORDER) - SUIT_ORDER.index(card.suit)
    if game_type == GameType.GEIER:
        return len(SUIT_ORDER) - SUIT_ORDER.index(card.suit)
    
    # Sauspiel oder Farb-Solo: Ober > Unter > Farbe
    if card.rank == Rank.OBER:
        return 14 - SUIT_ORDER.index(card.suit)
    elif card.rank == Rank.UNTER:
        return 10 - SUIT_ORDER.index(card.suit)
    return len(RANK_ORDER) - RANK_ORDER.index(card.rank)

def get_effective_suit(card: Card, game_type: GameType, trump_suit: Suit | None = None) -> str:
    if is_trumpf(card, game_type, trump_suit):
        return "TRUMPF"
    return card.suit.value