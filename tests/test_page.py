"""
TODO: input test description here
"""

import os
import os.path

import pageshot

TEST_URL = "https://www.bbc.co.uk/"
TEST_FILE = "out.png"


def test_taking_screenshot():
    if os.path.isfile(TEST_FILE):
        os.remove(TEST_FILE)
    ps = pageshot.Screenshoter()
    ps.take_screenshot(TEST_URL, TEST_FILE)
    assert os.path.isfile(TEST_FILE)
