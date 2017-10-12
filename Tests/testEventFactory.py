import unittest
from Models.MatchEventFactory import MatchEventFactory, MatchEventType

class TestEventFactory(unittest.TestCase):

    def setUp(self):
        self.factory = MatchEventFactory()
        self.matchEvent = self.factory.get_match_event(MatchEventType.GOAL, 10, 'SAMPLE MATCH', 'SAMPLE PLAYER')

    def test_setup(self):
        expected_time = 10
        expected_match = 'SAMPLE MATCH'
        expected_player = 'SAMPLE PLAYER'

        self.assertEqual(expected_time, self.matchEvent.time)
        self.assertEqual(expected_match, self.matchEvent.match)
        self.assertEqual(expected_player, self.matchEvent.player)