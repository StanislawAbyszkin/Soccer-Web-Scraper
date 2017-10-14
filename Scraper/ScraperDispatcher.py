import threading
import random
import logging
import time
import urllib2

class Dispatcher(object):
    MIN_WAIT_TIME = 0.3 # seconds
    MAX_WAIT_TIME = 2 # seconds

    logging.basicConfig(level=logging.DEBUG,
                        format='(%(threadName)-9s) %(message)s', )

    def __init__(self):
        self.lock = threading.Lock()

    def download(self, url):
        logging.debug('Acquiring lock')
        self.lock.acquire()
        wait_time_random = random.uniform(self.MIN_WAIT_TIME, self.MAX_WAIT_TIME)
        try:
            logging.debug('About to wait for %0.02f', wait_time_random)
            time.sleep(wait_time_random)
            return self.__download_url(url)
        finally:
            logging.debug('Finished downloading url: '+ url)
            self.lock.release()
            logging.debug('Lock released')
        raise IOError('Couldn''t download requested url: '+url)

    def __download_url(self,url):
        request = urllib2.Request(url)
        return urllib2.urlopen(request).read()


