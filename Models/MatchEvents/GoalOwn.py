from MatchEvent import MatchEvent

class GoalOwn(MatchEvent):
    def __init__(self, time, match, player):
        MatchEvent.__init__(self, time, match, player)