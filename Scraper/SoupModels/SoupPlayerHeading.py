from Soup import Soup
import re

class PlayerHeadingSoup(Soup):

    def __init__(self,soup):
        Soup.__init__(self, soup)

    def extract_name_surname(self):
        firstname, surname = re.sub(r'\(\d*\'\)', '',
                      self.get_soup().find('div', class_='player-name').text).strip().split()
        return firstname, surname

    def extract_number(self):
        return int(self.get_soup().find('div', class_='player-nr').text.strip())

    def extract_player_details_url(self):
        return self.get_soup().find('a')['href']

    def extract_player_given_id(self):
        return  re.search(r'\d*\.html\Z', self.__extract_player_details_url()).group(0).split('.')[0]

