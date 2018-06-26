"""
__________________________________________________
Base Page that provides basic page functionality

    Positional arguments:
    Selenium webdriver instance.
__________________________________________________
"""
from bs4 import BeautifulSoup
from random import randint
import time
import logging
import requests
# import os
# import csv

# from enchant import DictWithPWL
# from enchant.checker import SpellChecker
# from enchant.tokenize import EmailFilter

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select


class AbstractBasePage(object):
    """ Base Page object that provides basic page functionality.

    Positional arguments:
    Selenium webdriver instance.

    """
    PATH = '/'
    EXIT_PATH_URL = 'https://www.facebook.com'

    _timeout = 40

    _FOCUS_TAG_LOCATOR = (By.CSS_SELECTOR, 'body')
    _CLOSE_LOGIN_MODEL_BUTTON_LOCATOR = (By.CSS_SELECTOR, '[style*="block"] .close')
    _LOCATOR = (By.CSS_SELECTOR, 'div[class*="row"]')
    _MAIN_CSS_FILE_LOCATOR = (By.CSS_SELECTOR, 'title ~ link[href*="css/main"]')
    _LIB_JS_FILE_LOCATOR = (By.CSS_SELECTOR, 'script[src*="commons/libs."]')
    _PUBLIC_JS_FILE_LOCATOR = (By.CSS_SELECTOR, 'script[src*="public."]')
    _ALL_CDN_SCRIPT_LOCOS = (By.CSS_SELECTOR, 'script[src]')

    _LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'a[href^="/login/"]')
    _HOMEPAGE_COMPANY_LOGO_LOCATOR = (By.CSS_SELECTOR, 'img.logo')

    _HOPSCOTCH_CLOSE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.hopscotch-close')

    _SPELLING_CHECKER1_LOCATOR = (By.CSS_SELECTOR, '.internal-navbar-wrapper + .row')
    _SPELLING_CHECKER2_LOCATOR = (By.CSS_SELECTOR, '.internal-nav.nav')

    #
    #   Page Level Functions for inheriting classes
    #   Kundiddate : 9797969676

    def __init__(self, *args, **kwargs):

        self.selenium = args[0]
        logging.debug("kwargs:", kwargs)

    def go_to_page(self):
        url = self.PATH
        self.selenium.get(url)

    def refresh(self):
        self.selenium.refresh()

    def maximize(self):
        self.selenium.maximize_window()

    def go_to(self, path):
        self.selenium.get(path)


    def click_on_element(
            self,
            locator=None,
            index=None,
            exit_path=EXIT_PATH_URL):
        click_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(locator))
            WebDriverWait(self.selenium, self._timeout).until(
                EC.element_to_be_clickable(locator))

            button_link = self.selenium.find_elements(*locator)

            if index is None:
                if len(button_link) > 1:
                    index = randint(0, len(button_link)-1)
                else:
                    index = 0
            time.sleep(0.5)
            button_link[index].click()
            click_result = True

        finally:
            return click_result

    def enter_field_input(
            self,
            input_locator=_FOCUS_TAG_LOCATOR,
            values="No Input",
            exit_path=EXIT_PATH_URL):
        fill_result = False
        try:
            WebDriverWait(self.selenium, self._timeout).until(
                EC.presence_of_element_located(input_locator))
            WebDriverWait(self.selenium, self._timeout).until(
                EC.visibility_of_element_located(input_locator))

            name_field = self.selenium.find_element(*input_locator)
            time.sleep(0.5)
            name_field.send_keys(Keys.CONTROL + 'a')
            name_field.send_keys(Keys.BACKSPACE)
            name_field.send_keys(str(values))
            fill_result = True
        except Exception as e:
            print("\n Got exception, which is apparently : ")
            print("\n", e)

        finally:
            return fill_result

    def select_using_select(self, locator, value):
        return Select(self.selenium.find_element(*locator)).select_by_value(value)

