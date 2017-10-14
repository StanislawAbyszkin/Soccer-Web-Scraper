from Soup import Soup
from SoupPlayerHeading import PlayerHeadingSoup

class SquadsSoup(Soup):

    def __init__(self, soup):
        Soup.__init__(self, soup)

    def extract_hometeam_squad_first(self):
        '''
        :return: list of PlayerHeadingSoups of hometeam's first squad
        '''
        return self.__get_PlayersHeadingSoup_list(self.__get_soup_hometeam_squad_first)

    def extract_hometeam_squad_reserves(self):
        '''
        :return: list of PlayerHeadingSoups of hometeam's reserves squad
        '''
        return self.__get_PlayersHeadingSoup_list(self.__get_soup_hometeam_squad_reserves)

    def extract_awayteam_squad_first(self):
        '''
        :return: list of PlayerHeadingSoups of awayteam's first squad
        '''
        return self.__get_PlayersHeadingSoup_list(self.__get_soup_awayteam_squad_first)

    def extract_awayteam_squad_reserves(self):
        '''
        :return: list of PlayerHeadingSoups of awayteam's reserves squad
        '''
        return self.__get_PlayersHeadingSoup_list(self.__get_soup_awayteam_squad_reserves)

    def extract_hometeam_coach(self):
        return self.get_soup().find('section', class_='report-teams-players grid') \
            .find_all('span', class_='coach-name')[0].string.strip()

    def extract_awayteam_coach(self):
        return self.get_soup().find('section', class_='report-teams-players grid') \
            .find_all('span', class_='coach-name')[1].string.strip()

    def __get_PlayersHeadingSoup_list(self, methodToUse):
        players = []
        for player_heading_soup in methodToUse():
            player = PlayerHeadingSoup(str(player_heading_soup))
            players.append(player)
        return players

    def __get_soup_hometeam_squad_first(self):
        return self.get_soup()\
            .find('section', class_='report-teams-players grid').div\
            .find_all('div', class_='report-players-list grid')[0]\
            .find_all('a')

    def __get_soup_hometeam_squad_reserves(self):
        return self.get_soup()\
            .find('section', class_='report-teams-players grid').div\
            .find_all('div', class_='report-players-list grid')[1]\
            .find_all('a')

    def __get_soup_awayteam_squad_first(self):
        return self.get_soup() \
            .find('section', class_='report-teams-players grid')\
            .find('div', class_='grid-24 grid-msw-48 grid-ms-48 text-right')\
            .find_all('div', class_='report-players-list text-right grid')[0]\
            .find_all('a')

    def __get_soup_awayteam_squad_reserves(self):
        return self.get_soup()\
            .find('section', class_='report-teams-players grid')\
            .find('div', class_='grid-24 grid-msw-48 grid-ms-48 text-right')\
            .find_all('div', class_='report-players-list text-right grid')[1]\
            .find_all('a')