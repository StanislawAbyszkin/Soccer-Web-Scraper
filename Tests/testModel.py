# -*- coding: utf-8 -*-
import unittest
from Models.Match import Match

class TestMatchModel(unittest.TestCase):

    def setUp(self):
        dict = {'date':'2017-08-17',
                'home_team':'Naprzód Brwinów',
                'away_team': 'Znicz Pruszków'}
        self.match = Match(**dict)

    def test_match_model_set_up(self):
        expected_date = '2017-08-17'
        expected_home_team = 'Naprzód Brwinów'
        expected_away_team = 'Znicz Pruszków'

        self.assertEqual(expected_date,self.match.date)
        self.assertEqual(expected_home_team, self.match.home_team)
        self.assertEqual(expected_away_team, self.match.away_team)
        self.assertIs(self.match.gameType, None)

    def test_match_model_set_up2(self):
        self.assertIs(None, None)


if __name__ == '__main__':
    unittest.main()