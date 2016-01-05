import os

from selenium import webdriver

BASE_FOLDER = os.path.dirname(os.path.realpath(__file__))


class Screenshoter(object):

    def __init__(self, width=1024, height=768):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(width, height)
        # record height for truncating
        self.height = height

    def take_screenshot(self, url, filename):
        """
        Take screenshot of a URL.

        See http://stackoverflow.com/questions/13287490/is-there-a-way-to-use-phantomjs-in-python

        :param url_filename: dict of url to filename
        :type url_filename: dict
        """
        try:
            os.remove(filename)
        except OSError:
            pass
        self.driver.get(url)
        self.driver.save_screenshot(filename) # save a screenshot to disk
