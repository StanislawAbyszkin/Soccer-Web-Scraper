from Soup import Soup
from EnumTeamType import TeamType
import re

class MatchDetailsSoup(Soup):

    def __init__(self,soup):
        Soup.__init__(self, soup)

    def extract_gameweek(self):
        result = self.get_soup().find('section', class_='report-result-logos grid')
        if result is not None:
            gameweek = result.find('h1').text.strip()
            gameweek = re.search(r'(\d+)', gameweek).group(0)
            return gameweek
        raise ValueError('Match details do not contain data on gameweek')

    def extract_team_name(self, team_type=TeamType.HOME_TEAM):
        wynik = self.get_soup().find('section', class_='report-result-logos grid')

        list_position = 0 if team_type == TeamType.HOME_TEAM else 2

        if wynik is not None:
            return wynik.find_all('div')[list_position].text.strip()

        return None

    def extract_team_id(self, team_type=TeamType.HOME_TEAM):
        wynik = self.get_soup().find('section', class_='report-result-logos grid')

        list_position = 0 if team_type == TeamType.HOME_TEAM else 2

        if wynik is not None:
            team_link = wynik.find_all('div')[list_position].find_all('a')[1]['href']
            return re.search(r'\d*\.html\Z', team_link).group(0).split('.')[0]

        return None

    def extract_team_goals(self, team_type=TeamType.HOME_TEAM):
        wynik = self.get_soup().find('section', class_='report-result-logos grid')

        list_position = 0 if team_type == TeamType.HOME_TEAM else 1

        if wynik is not None:
            return wynik.find_all('div')[1].text.strip().split(':')[list_position]

        return None

    def extract_team_weblink(self, team_type=TeamType.HOME_TEAM):
        wynik = self.get_soup().find('section', class_='report-result-logos grid')

        list_position = 0 if team_type == TeamType.HOME_TEAM else 2

        if wynik is not None:
            return wynik.find_all('div')[list_position].find_all('a')[1]['href']

        return None

    def extract_players_soup(self):
        players_soup = self.get_soup().find('section', class_='report-teams-players grid')
        return players_soup

    def extract_match_events_soup(self):
        match_events_soup = self.get_soup().find('section', class_='box-standard no-mb')
        return match_events_soup

