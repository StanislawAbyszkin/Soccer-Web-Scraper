# -*- coding: utf-8 -*-
import unittest
from DataForTests import match_events_text, match_event_heading_text
from Scraper.SoupMatchEvents import MatchEventsSoup
from Scraper.SoupMatchEventsHeading import MatchEventsHeadingSoup

class TestMatchEventsSoup(unittest.TestCase):

    def setUp(self):
        self.soup = MatchEventsSoup(match_events_text)

    def test_count_of_events(self):
        expected = 28
        actual = len(self.soup.extract_all_events())

        self.assertEqual(expected,actual)


class TestMatchEventHeading(unittest.TestCase):

    def setUp(self):
        self.soup = MatchEventsHeadingSoup(match_event_heading_text)

    def test_event_time(self):
        expected = 85
        actual = self.soup.get_event_time()

        self.assertEqual(expected, actual)

    def test_event_player_id(self):
        expected = 738907
        actual = self.soup.get_event_player_id()

        self.assertEqual(expected, actual)
