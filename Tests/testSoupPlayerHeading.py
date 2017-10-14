# -*- coding: utf-8 -*-
import unittest

from DataForTests import player_heading_text
from Scraper.SoupModels.SoupPlayerHeading import PlayerHeadingSoup


class TestPlayersSoup(unittest.TestCase):

    def setUp(self):
        self.soup = PlayerHeadingSoup(player_heading_text)


    def test_get_name_method(self):
        expected_name = u'Rafał'
        expected_surname = u'Fajger'

        actual_name, actual_surname = self.soup.extract_name_surname()

        self.assertEqual(expected_name, actual_name, 'Names are not matching')
        self.assertEqual(expected_surname, actual_surname, 'Surnames are not matching')


    def test_get_number_method(self):
        expected = 8
        actual = self.soup.extract_number()

        self.assertEqual(expected,actual)

    def test_get_url_method(self):
        expected = 'https://www.laczynaspilka.pl/zawodnik/rafal-fajger,726244.html'
        actual = self.soup.extract_player_details_url()

        self.assertEqual(expected,actual)
