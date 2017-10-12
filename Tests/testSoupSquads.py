# -*- coding: utf-8 -*-

import unittest
from DataForTests import squads_text
from Scraper.SoupSquads import SquadsSoup

class TestPlayersSoup(unittest.TestCase):

    def setUp(self):
        self.soup = SquadsSoup(squads_text)

    def test_home_team_squad_size(self):
        expected = 11
        actual_hometeam = len(self.soup.extract_hometeam_squad_first())
        actual_awayteam = len(self.soup.extract_awayteam_squad_first())

        self.assertEqual(expected,actual_hometeam)
        self.assertEqual(expected,actual_awayteam)

    def test_coaches_names(self):
        expected_hometeam_coach = u'Kwaśniewski Tomasz'
        expected_awayteam_coach = u'Korbuszewski Hubert'

        actual_hometeam_coach = self.soup.extract_hometeam_coach()
        actual_awayeam_coach = self.soup.extract_awayteam_coach()

        self.assertEqual(expected_hometeam_coach, actual_hometeam_coach)
        self.assertEqual(expected_awayteam_coach, actual_awayeam_coach)
