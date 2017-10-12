from abc import ABCMeta, abstractmethod

class MatchEvent(object):
    def __init__(self, time, match, player):
        self.time = time
        self.match = match
        self.player = player