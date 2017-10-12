from MatchEvents import *
from EnumMatchEventType import MatchEventType

class MatchEventFactory(object):

    def get_match_event(self, requested_event, time, match, player):

        if requested_event is MatchEventType.GOAL:
            return Goal(time, match, player)
        elif requested_event is MatchEventType.GOAL_OWN:
            return GoalOwn(time, match, player)
        elif requested_event is MatchEventType.CARD_RED:
            return CardRed(time, match, player)
        elif requested_event is MatchEventType.CARD_YELLOW:
            return CardYellow(time, match, player)
        elif requested_event is MatchEventType.PLAYER_START:
            return PlayerStarting(time, match, player)
        elif requested_event is MatchEventType.PLAYER_END:
            return PlayerEnding(time, match, player)
        elif requested_event is MatchEventType.SUB_OFF:
            return SubstitutionOff(time, match, player)
        elif requested_event is MatchEventType.SUB_ON:
            return SubstitutionOn(time, match, player)

        raise ValueError('Wrong type of match event passed')