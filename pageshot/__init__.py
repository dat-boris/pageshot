import os

from selenium import webdriver
import PIL
from PIL import Image

BASE_FOLDER = os.path.dirname(os.path.realpath(__file__))

DEFAULT_WIDTH = 1024
DEFAULT_HEIGHT = 768


class Screenshoter(object):

    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(width, height)
        # record height for truncating
        self.width = width
        self.height = height

    def __del__(self):
        # TODO: still cause issue with phantomjs not closing :-(
        self.driver.close()
        self.driver.quit()

    def take_screenshot(self, url, filename, thumbnail=True):
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
        self.driver.save_screenshot(filename)  # save a screenshot to disk
        if thumbnail:
            self.make_thumbnail(filename)

    @classmethod
    def make_thumbnail(cls, img_file,
                       thumbnail_width=512,
                       outfile=None,
                       default_width=DEFAULT_WIDTH,
                       default_height=DEFAULT_HEIGHT):
        if not outfile:
            outfile = img_file
        img = Image.open(img_file)
        w, h = img.size
        img = img.crop((0, 0, w, default_height))

        ratio = 1. * thumbnail_width / default_width
        img.thumbnail((
            w * ratio, default_height * ratio
        ), Image.ANTIALIAS)
        img.save(outfile)
