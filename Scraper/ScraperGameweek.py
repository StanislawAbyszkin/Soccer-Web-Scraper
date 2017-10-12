import HelperMethods
class GameweekScraper(object):

    def __init__(self,gameweek_url, gameweek):
        self.gameweek_url = gameweek_url
        self.gameweek = gameweek

    def start_downloading_data(self):
        pass

    def _url_for_gameweek(self):
        return str(self.gameweek_url) + "?round=" + str(self.gameweek)