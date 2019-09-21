#!/usr/bin/env python

"""
test_kitten_bomb.py: Uses Selenium and Pytest to showcase testing automation.
"""



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
	Kitty Bomb uses an array of all the images labeled 'Image result for Fluffy Kittens' on the search page.
	It then clicks each image and opens a new window. Bomb is the array of images and with the for loop it will go
	through every item in the array and store the item in picture. It then uses an Action Chain which holds down
	shift when you click the image. This makes sure the image will open in a new window. From there it opens 100
	images of kittens in a new window.
	:param browser:
	"""
	page = PagePOM(browser)
	page.load()
	page.search_for('Fluffy Kittens')
	page.kitten_bomb()
	# comment this out
	browser.quit()

def test_save(browser):
	"""
	Kitty Save takes the working directory of the project and then it goes through the first 10 of the Bomb array
	and saves them inside a folder in the directory.
	:param browser:
	"""
	page = PagePOM(browser)
	page.load()
	page.search_for('Fluffy Kittens')
	page.kitten_save()
	# comment this out
	browser.quit()
