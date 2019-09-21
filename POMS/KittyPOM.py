#!/usr/bin/env python

"""
KittyPOM.py: .
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging

__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Kitten Bomb"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


class PagePOM(object):
    """
    This is the Page Object Model used in test_forms_Page.py for the filling out forms section
    of Ultimate QA's Automation Exercises.
    """
    URL = 'https://images.google.com'

    search = (By.NAME, 'q')
    kittens = (By.CSS_SELECTOR, "img[alt='Image result for Fluffy Kittens']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search_for(self, phrase):
        search_input = self.browser.find_element(*self.search)
        search_input.send_keys(phrase)
        search_input.submit()

    def get_search_array(self):
        return self.browser.find_element(*self.kittens)

    def kitten_bomb(self):
        bomb = self.browser.find_elements(*self.kittens)
        logging.info(len(bomb))
        # for picture in bomb:  # .click(picture) \
        i = 0
        while i < 10:
            ActionChains(self.browser) \
                .key_down(Keys.SHIFT) \
                .click(bomb[i]) \
                .key_up(Keys.SHIFT) \
                .perform()
            i += 1
