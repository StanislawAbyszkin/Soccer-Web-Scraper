from enum import Enum

class MatchEventType(Enum):
    CARD_RED = 1
    CARD_YELLOW = 2
    GOAL = 3
    GOAL_OWN = 4
    PLAYER_END = 5
    PLAYER_START = 6
    SUB_OFF = 7
    SUB_ON = 8