# Kitty Bomb
Kitty Bomb is a program that will: 
- A) search Google and open up a bunch of images of kittens 
- B) search Google and save the thumb nails of the cat images into a folder.

## Badges
![GitHub](https://img.shields.io/github/license/GirlsCodeLincoln/kitty-bomb.svg) ![GitHub issues](https://img.shields.io/github/issues-raw/GirlsCodeLincoln/kitty-bomb.svg) [![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/benweese/python-automation)

## Motivation
This was created for [Girls Code Lincoln](https://girlscodelincoln.com/) to teach automation hopefully.

## Tools
<b>Built with</b>
- [Pycharm Community](https://www.jetbrains.com/pycharm/)

<b>Testing Language</b>
- [Selenium](https://www.seleniumhq.org/)

<b>Continuous Integration</b>
- [CircleCI](https://circleci.com/)

<b>Dependency Maintenance </b>
- [Dependabot by Github](https://dependabot.com/)

<b>Downloads</b>
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [pip3](https://pip.pypa.io/en/stable/)
- [pipenv](https://docs.pipenv.org/en/latest/)
- [Python3](https://www.python.org/download/releases/3.0/)


## Features
With uses our Circle-CI runner using pipenv and pytest to run our automation scripts in Command line.

## Page Being Automated
[Google Image Search](https://images.google.com)

## Code Example
<b>Kitty Bomb</b>
```
def kitten_bomb(self):
    bomb = self.browser.find_elements(*self.kittens)
    for picture in bomb:  
        ActionChains(self.browser) \
            .key_down(Keys.SHIFT) \
            .click(picture) \
            .key_up(Keys.SHIFT) \
            .perform()
```
<b>Kitty Save</b>
```
def kitten_save(self):
    path = os.getcwd()
    bomb = self.browser.find_elements(*self.kittens)
    i = 0
    while i < 10:
        url = bomb[i].get_attribute("src")
        urllib.request.urlretrieve(url, path + "/test-results/kittens/kitty-" + str(i) + ".jpg")
        i += 1
```

## Documentation
Kitty Bomb uses an array of all the images labeled 'Image result for Fluffy Kittens' on the search page. It then clicks each image and opens a new window. Bomb is the array of images and with the for loop it will go through every item in the array and store the item in picture. It then uses an Action Chain which holds down shift when you click the image. This makes sure the image will open in a new window. From there it opens 100 images of kittens in a new window.

Kitty Save takes the working directory of the project and then it goes through the first 10 of the Bomb array and saves them inside a folder in the directory. 

## Credits
[Ben Weese](https://benweese.dev)
