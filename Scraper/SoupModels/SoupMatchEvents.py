from Soup import Soup

class MatchEventsSoup(Soup):

    def __init__(self,soup):
        Soup.__init__(self, soup)

    def __get_all_events(self):
        return self.get_soup()\
            .find('div', class_='toggle-content')\
            .find_all('div', class_='report-tracking-action padding-0-10 grid')

    def extract_all_events(self):
        return self.__get_all_events()
