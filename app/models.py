from enum import Enum

class Suit(str, Enum):
    EICHEL = "E"
    GRAS = "G"
    HERZ = "H"
    SCHELLEN ="S"

class Rank(str, Enum):
    OBER = "O"
    UNTER = "U"                                                                                                                                                                                                                      
    ASS = "A"
    ZEHN = "Z"                                                                                                                                                                                                                       
    KOENIG = "K"                                                                                                                                                                                                                   
    NEUN = "9"
    ACHT = "8"
    SIEBEN = "7"    

class GameType(str, Enum):
    SAUSPIEL = "Sauspiel"
    WENZ = "Wenz"
    FARB_SOLO = "Farb-Solo"
    GEIER = "Geier"

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.suit.value}{self.rank.value}"
    
    def __eq__(self, other: object) -> bool:                                                                                                                                                                                       
        if not isinstance(other, Card):
            return False                                          
                                                                                                                                                                               
        return self.suit == other.suit and self.rank == other.rank    
    
    def __hash__(self) -> int:                                                                                                                                                                                                     
        return hash((self.suit, self.rank))

    @staticmethod                                                                                                                                                                                                                    
    def from_str(code: str) -> "Card":
        return Card(Suit(code[0]), Rank(code[1:]))