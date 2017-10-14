import HelperMethods
import Scraper

class GameweekScraper(Scraper):

    def __init__(self,gameweek_url, gameweek):
        self.gameweek_url = gameweek_url
        self.gameweek = gameweek

    def download_soup(self):
        pass

    def get_download_url(self):
        return str(self.gameweek_url) + "?round=" + str(self.gameweek)