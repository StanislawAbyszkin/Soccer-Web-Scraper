# -*- coding: utf-8 -*-
import unittest
from Scraper import Soup, GameweekSoup, LeagueSoup
from DataForTests import  gameweek_text

class TestSoup(unittest.TestCase):

    def setUp(self):
        self.soup = Soup('<html><body><p>Some basic soup instance</p></body></html>')

    def test_soup_initialisation(self):
        expectedSoup = '<html><body><p>Some basic soup instance</p></body></html>'
        self.assertEqual(str(self.soup.get_soup()), expectedSoup)

    def test_soup_basic_funcionality(self):
        expected = 'Some basic soup instance'
        actual = self.soup.get_soup().p.string

        self.assertEqual(expected,actual)

class TestGameweekSoup(unittest.TestCase):

    def setUp(self):
        self.gameweek_soup = GameweekSoup(gameweek_text)

    def test_get_gameweek_number(self):
        expected = 8
        actual = len(self.gameweek_soup.get_match_headings())

        self.assertEqual(expected,actual)

    def test_gameweek_first_game_home_team(self):
        expected = u'GKS Naprzód GOSIR Stare Babice'
        actual = self.gameweek_soup.get_match_headings()[0].find('a', class_='team').string

        self.assertEqual(expected,actual)

class TestLeagueSoup(unittest.TestCase):

    def setUp(self):
        self.league_soup = LeagueSoup()

if __name__ == '__main__':
    unittest.main()