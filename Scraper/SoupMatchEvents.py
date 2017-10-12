from Soup import Soup
from SoupMatchEventsHeading import MatchEventsHeadingSoup

class MatchEventsSoup(Soup):

    def __init__(self,soup):
        Soup.__init__(self, soup)

    def __get_all_events(self):
        return self.get_soup()\
            .find('div', class_='toggle-content')\
            .find_all('div', class_='report-tracking-action padding-0-10 grid')

    def extract_all_events(self):
        return self.__get_all_events()

    def get_event_type(self):
        events = []
        for event_soup in self.__get_all_events():
            event = MatchEventsHeadingSoup(str(event_soup))
            events.append(event.get_event_type())
        return events
