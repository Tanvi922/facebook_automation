from __future__ import print_function

import string

import nose.tools
import nose.plugins.multiprocess
from django.utils.crypto import get_random_string
from nose.plugins.attrib import attr

from testing.test_base_class import BaseTest
from testing.page_classes.facebook import *



@attr()
# @attr(type="run")
class TestFacebookRegistration(BaseTest):

    _FNAME = 'Tanvi'
    _LNAME = 'Joshi'
    _EMAIL = get_random_string() + '@gmail.com'
    _EMAIL_LOGIN = 'tanvitestingdemo@gmail.com'
    _DAY = str(randint(0, 28))
    _YEAR = str(randint(1952, 2000))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # _MONTH = months[randint(0, len(months) - 1)]
    _MONTH = str(randint(1,12))
    _GENDER = randint(0, 1)
    _PASSWORD = 'Tanvi123456'

    @classmethod
    def setUpClass(self):
        super(TestFacebookRegistration, self).setUpClass()
        self.home_page = FacebookBasePage(self._browser)
        self.home_page.go_to_page()
        self.home_page.maximize()

    def test_00_fill_registration_form(self):
        nose.tools.assert_true(self.home_page.
                               fill_complete_details_to_register
                               (self._FNAME,self._LNAME,self._EMAIL
                                ,self._PASSWORD,self._DAY,
                                self._MONTH,self._YEAR,self._GENDER))

    def test_01_logout_user(self):
        nose.tools.assert_true(self.home_page.logout_user)

    def test_02_login_user(self):
        nose.tools.assert_true(self.home_page.login_user(self._EMAIL_LOGIN, self._PASSWORD))

    def test_03_search_for_friend(self):
        nose.tools.assert_true(self.home_page.search_for_friend)

    def test_04_send_friend_request(self):
        nose.tools.assert_true(self.home_page.send_friend_request)

    def test_05_logout_user(self):
        nose.tools.assert_true(self.home_page.logout_user)

