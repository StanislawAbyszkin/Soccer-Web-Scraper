import abc

class Scraper(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_download_url(self):
        '''get URL for downloading specific Soup'''
        return