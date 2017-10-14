from Soup import Soup
from datetime import datetime, time, date

class MatchHeadingSoup(Soup):

    def __init__(self,soup):
        Soup.__init__(self, soup)

    def get_date_of_match(self):
        month_year = self.get_soup().find('span', class_='month').text.strip().split('/')
        hour_min = self.get_soup().find('span', class_='hour').text.strip().split(':')

        # Find date of the game
        day = int(self.get_soup().find('span', class_='day').text.strip())
        month = int(month_year[0])
        year = int(month_year[1])

        # Find hour of the game
        hour = int(hour_min[0])
        minute = int(hour_min[1])

        # Combine date and time together
        d = date(year, month, day)
        t = time(hour, minute)

        return datetime.combine(d, t)

    def get_match_detail_url(self):
        return self.get_soup().find('div', class_='season__game-action grid-16 grid-mt-12 grid-msw-48').a['href']
