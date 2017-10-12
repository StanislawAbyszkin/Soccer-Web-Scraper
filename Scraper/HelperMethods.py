import re
import urllib2
from bs4 import BeautifulSoup

def extract_player_id_from_url(url):
    '''
    Helper function for geting player_id from url.
    :return: ID number of player.
    '''
    player_id = re.search(r'\d*\.html\Z', url).group(0).split('.')[0]
    return player_id

def connect_and_download_soup(self, url):
    '''
    Helper function for getting soup from specified URL.
    :param url: URL for website you want to parse.
    :return: BeautifulSoup soup with soup.
    '''
    request = urllib2.Request(url)
    sauce = urllib2.urlopen(request).read()
    return BeautifulSoup(sauce, 'lxml')