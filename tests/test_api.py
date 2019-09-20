"""
Placeholder
"""
import requests

URL_API = 'https://swapi.co/api/people/1'


def api_call():
	"""
	Gets the films listed in the api.
	:param episode:
	:return: response json
	"""
	response = requests.get(URL_API)
	return response


def test_1():
	"""
	Asserts that a 200 was returned
	:param episode:
	"""
	assert api_call().status_code == 200


def test_2():
	"""
	This checks that all the films are in the response.
	:param name:
	:param episode:
	"""
	name = "Luke Skywalker"
	assert name.lower() == api_call().json()['name'].lower()

