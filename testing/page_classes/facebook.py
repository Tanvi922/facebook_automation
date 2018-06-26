from __future__ import print_function
import time
import requests
from random import randint, randrange

import nose.tools
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from testing.page_classes.page_base import AbstractBasePage


class FacebookBasePage(AbstractBasePage):

     PATH = 'www.facebook.com'
    _FIRST_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, '[aria-label="First name"]')
    _LAST_NAME_INPUT_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Surname"]')
    _MOBILE_EMAIL_INPUT_FILED_LOCATOR = (By.CSS_SELECTOR, '[name="reg_email__"]')
    _CON_EMAIL_INPUT_FILED_LOCATOR = (By.CSS_SELECTOR, '[name="reg_email_confirmation__"]')
    _PASSWORD_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, '[data-type="password"]')
    _DOB_DAY_DROPDOWN_LOCATOR = (By.ID, 'day')
    _DOB_MONTH_DROPDOWN_LOCATOR = (By.ID, 'month')
    _DOB_YEAR_DROPDOWN_LOCATOR = (By.ID, 'year')
    _GENDER_RADIO_BTN_LOCATOR = (By.CSS_SELECTOR, '[name= "sex"]')
    _SIGN_UP_BTN_LOCATOR = (By.CSS_SELECTOR, '[name="websubmit"]')
    _NAVBAR_DROPDOWN_LOCATOR = (By.ID, 'pageLoginAnchor')
    _LOGOUT_LOCATOR = (By.CSS_SELECTOR, 'a[data-gt*="menu_logout"]')
    _LOGOUT_CON_BTN_LOCATOR = (By.CSS_SELECTOR, '.uiOverlayButton[type="submit"]')
    _LOGIN_EMAIL_LOCATOR = (By.ID, 'email')
    _LOGIN_PASSWORD_LOCATOR = (By.ID, 'pass')
    _LOGIN_BTN_LOCATOR = (By.ID, 'loginbutton')
    _SEARCH_INPUT_LOCATOR = (By.CSS_SELECTOR, '[name="q"]')
    _SEARCH_BTN_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Search"] i')
    _SEARCH_BY_PPL_LOCATOR = (By.CSS_SELECTOR, '[data-edge="keywords_users"]')
    _SEND_FRIEND_REQUEST = (By.CSS_SELECTOR, '#u_ps_jsonp_4_3_a')

    def fill_complete_details_to_register(self, fname,lname,email,password,day,month,year,gender):
        res1 = self.enter_field_input(self._FIRST_NAME_INPUT_LOCATOR, fname)
        res2 = self.enter_field_input(self._LAST_NAME_INPUT_LOCATOR, lname)
        res3 = self.enter_field_input(self._MOBILE_EMAIL_INPUT_FILED_LOCATOR, email)
        res4 = self.enter_field_input(self._CON_EMAIL_INPUT_FILED_LOCATOR, email)
        res5 = self.enter_field_input(self._PASSWORD_INPUT_FIELD_LOCATOR, password)
        res6 = self.select_using_select(self._DOB_DAY_DROPDOWN_LOCATOR, day)
        res7 = self.select_using_select(self._DOB_MONTH_DROPDOWN_LOCATOR, month)
        res8 = self.select_using_select(self._DOB_YEAR_DROPDOWN_LOCATOR, year)
        res9 = self.click_on_element(self._GENDER_RADIO_BTN_LOCATOR, gender)
        res10 = self.click_on_element(self._SIGN_UP_BTN_LOCATOR)
        print(res1,res2,res3,res4,res5,res6,res7,res8,res9,res10)
        time.sleep(10)
        return True

    @property
    def logout_user(self):
        self.click_on_element(self._NAVBAR_DROPDOWN_LOCATOR)
        self.click_on_element(self._LOGOUT_LOCATOR)
        return self.click_on_element(self._LOGOUT_CON_BTN_LOCATOR)

    def login_user(self,email,password):
        self.enter_field_input(self._LOGIN_EMAIL_LOCATOR,email)
        self.enter_field_input(self._LOGIN_PASSWORD_LOCATOR,password)
        return self.click_on_element(self._LOGIN_BTN_LOCATOR)

    @property
    def search_for_friend(self):
        self.enter_field_input(self._SEARCH_INPUT_LOCATOR, 'tanvi joshi')
        self.click_on_element(self._SEARCH_BTN_LOCATOR)
        return self.click_on_element(self._SEARCH_BY_PPL_LOCATOR)

    @property
    def send_friend_request(self):
        return self.click_on_element(self._SEND_FRIEND_REQUEST)




