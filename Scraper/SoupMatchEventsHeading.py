from Models.EnumMatchEventType import MatchEventType
import HelperMethods
import re
from Soup import Soup

class MatchEventsHeadingSoup(Soup):

    def __init__(self,soup):
        Soup.__init__(self, soup)

    event_dict = {
        'i-report-ball': MatchEventType.GOAL,
        'i-yellow-card': MatchEventType.CARD_YELLOW,
        'i-red-card': MatchEventType.CARD_RED,
        'i-report-arrow-up': MatchEventType.SUB_ON,
        'i-report-arrow-down': MatchEventType.SUB_OFF
    }

    def get_event_type(self):
        event_name = self.get_soup().find('div', class_='action-icon grid-3 grid-mt-4 grid-msw-5 grid-ms-5').i['class'][0]
        event_type = self.event_dict[event_name]
        return event_type

    def get_event_time(self):
        return self.__extract_event_minute()

    def get_event_player_id(self):
        url = self.get_soup().find('a')['href']
        return int(HelperMethods.extract_player_id_from_url(url))

    def __extract_event_minute(self):
        minuta = self.get_soup().find('div', re.compile('action-time')).text.strip()
        minuta = re.search(r'(\d+\+\d+|\d+)', minuta)
        if minuta is not None:
            minuta = minuta.group(0)
            if re.search(r'\d+\+\d+', minuta):
                minuta = int(minuta.split('+')[0]) + int(minuta.split('+')[1])
        return int(minuta)