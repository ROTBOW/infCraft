import math
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

options = Options()
options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# options.add_argument('-headless')


# constants

SITE = r"https://neal.fun/infinite-craft/"


class Asphodel:

    def __init__(self) -> None:
        self.ingredients = list()
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(0.5)
