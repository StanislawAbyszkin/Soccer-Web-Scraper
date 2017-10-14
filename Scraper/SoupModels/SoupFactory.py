from Soup import Soup
from SoupRegion import  RegionSoup
from SoupMatchDetails import MatchDetailsSoup
from SoupGameweek import GameweekSoup


class SoupFactory(object):
    __soupList = ['Region','Match', 'Gameweek']

    def __init__(self):
        pass

    def get_soup(self, soup_type, soup):
        if soup_type == 'Region':
            return RegionSoup(soup)
        elif soup_type == 'Match':
            return MatchDetailsSoup(soup)
        elif soup_type == 'Gameweek':
            return GameweekSoup(soup)
        else:
            raise ValueError('Factory can\'t create soup')
