from Soup import Soup

class GameweekSoup(Soup):

    def __init__(self,soup,**kwargs):
        Soup.__init__(self, soup)
        self.__gameweek = kwargs.get('gameweek')

    def get_gameweek(self):
        return self.__gameweek

    def get_match_headings(self):
        """
        :return: List of matches in html form
        """
        return self.get_soup().find_all('article', class_='season__game grid')