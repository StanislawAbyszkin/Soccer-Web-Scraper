# -*- coding: utf-8 -*-
from Soup import Soup
import re

class LeagueSoup(Soup):

    def __init__(self,soup, league_name, league_url):
        Soup.__init__(self, soup)
        self.__league_name = league_name
        self.__url = league_url

    def get_league_id(self):
        if self.__url is not None:
            return re.search(r'\d*\.html\Z', self.__url).group(0).split('.')[0]
        else:
            raise ValueError('Url for league soup is not set')

    def get_league_url(self):
        return self.__url

    def get_league_level(self):
        league_levels = {
            'IV Liga': 5,
            'Klasa Okręgowa': 6,
            'A Klasa': 7,
            'B Klasa': 8,
            'C Klasa': 9,
        }
        for league_lvl in league_levels:
            if re.search(league_lvl, self.__league_name):
                return league_levels[league_lvl]

        raise ValueError('League name is not supported by get_league_level method')

    def get_league_name(self):
        return self.__league_name
