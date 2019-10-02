#!/usr/bin/env python

"""
KittyPOM.py: .
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import os

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

    # This fines the search element so we can use it. Kittens creates an array of the images to be selected.
    search = (By.NAME, 'q')
    kittens = (By.CSS_SELECTOR, "img[alt='Image result for Fluffy Kittens']")

    def __init__(self, browser):
        """
        This sets up the browser so we can use Google Chrome.
        :param browser:
        """
        self.browser = browser

    def load(self):
        """
        This opens chrome and goes to our URL.
        """
        self.browser.get(self.URL)

    def search_for(self, phrase):
        """
        We use search to create a web element of search, then we send it our search phrase and submit.
        :param phrase:
        """
        search_input = self.browser.find_element(*self.search)
        search_input.send_keys(phrase)
        search_input.submit()

    def kitten_bomb(self):
        """
        This opens up several windows with each being an image found in google.
        First we create a web element for the images.
        """
        bomb = self.browser.find_elements(*self.kittens)
        # The below comment is what we can use to go through all 100 images and open them in a new window.
        # However this eventually starts slowing down the computer.
        # for picture in bomb:  # .click(picture) \

        # We create a while loop so we can open the first 10 images.
        i = 0
        while i < 10:
            # An Action Chain is uses so we can hold down a key while we click.
            # In chrome if you hold shift and click it opens in an new window.
            # After we click the image and open it in a new window we key up
            # shift so the rest of our code isn't holding down shift.
            ActionChains(self.browser) \
                .key_down(Keys.SHIFT) \
                .click(bomb[i]) \
                .key_up(Keys.SHIFT) \
                .perform()
            i += 1

    def kitten_save(self):
        """
        This looks through google and then saves the first 10 images in a folder.
        """
        # This fines the location of our current working directory.
        path = os.getcwd()
        # we create a web element for the images.
        bomb = self.browser.find_elements(*self.kittens)
        # The below comment is what we can use to go through all 100 images and save them all.
        # for picture in bomb:  # .click(picture) \

        # We create a while loop so we can open the first 10 images.
        i = 0
        while i < 10:
            # This pulls the image's link so we know where to find the image.
            url = bomb[i].get_attribute("src")
            # This retrieves the URL then saves the image to the folder in our directory
            # with the name kitty and a number.
            urllib.request.urlretrieve(url, path + "/test-results/kittens/kitty-" + str(i) + ".jpg")
            i += 1