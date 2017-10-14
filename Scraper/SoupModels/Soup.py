from bs4 import BeautifulSoup

class Soup(object):

    def __init__(self,soup):
        self.__soup = BeautifulSoup(soup, "lxml")

    def get_soup(self):
        return self.__soup
