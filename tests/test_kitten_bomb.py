#!/usr/bin/env python

"""
test_kitten_bomb.py: Uses Selenium and Pytest to showcase testing automation.
"""

import time

from POMS.KittyPOM import PagePOM

__author__ = "Ben Weese"
__copyright__ = "Copyright 2019, Python Automation"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Ben Weese"
__email__ = "ben@benweese.dev"
__status__ = "refactor"


def test_bomb(browser):
	"""
	This fills out the First form on the page and makes sure the date was entered.
	Then it will verify if the message was successfully sent.
	:param browser:
	"""
	page = PagePOM(browser)
	page.load()
	page.search_for('Fluffy Kittens')
	page.kitten_bomb()
	# comment this out
	browser.quit()


