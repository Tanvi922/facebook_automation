"""
_________________________________________________

Test Class for Employer zone

        Log in function

_________________________________________________
"""
from __future__ import print_function
import time

import nose.tools
import nose.plugins.multiprocess
from nose.plugins.attrib import attr

from recruit.testing.test_base_class import BaseTest
from recruit.testing.page_classes.employer.employer_home import EmployerHomePage
from recruit.testing.page_classes.employer.employer_dashboard.dashboard_home import DashboardHomePage


@attr()
# @attr(type="run")
class Test00EmployerLogin(BaseTest):
    """ Test cases for Login Modal - Normal Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = '123456'

    @classmethod
    def setUpClass(self):
        super(Test00EmployerLogin, self).setUpClass()
        self.prod_employer_page = 'https://www.aasaanjobs.com/employer/'
        self.home_page = EmployerHomePage(self._browser)
        self.dash_home_page = DashboardHomePage(self._browser)
        self.home_page.go_to(self.prod_employer_page)
        # self.home_page.go_to_page()
        self.home_page.maximize()
        self.email = 'talentacquisition@aasaanjobs.com'

    # def tearDown(self):
    #     input("\n >> \t __ aint that roight? __ \t << ")

    def test_00_click_login_header(self):
        """00 Test Login Header button works"""
        nose.tools.assert_true(self.home_page.click_login_header)

    def test_01_valid_input_data_for_email_or_mobile(self):
        """01 Test Valid Mobiles/Emails for Login pass"""
        self.home_page.fill_mobile_or_email_id(self.email)
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)

    # def test_02_invalid_input_data_for_password(self):
    #     """02 Test Invalid Passwords for Login fail"""
    #     self.home_page.fill_invalid_password_values()

    def test_03_valid_input_data_for_password(self):

        nose.tools.assert_true(
            self.home_page.fill_password_field(self._PASSWORD)
        )
        nose.tools.assert_true(
            self.dash_home_page.check_for_new_url(
                self.dash_home_page.PATH
            )
        )

    def test_04_logout_user(self):
        """04 Test Logout function [for a Logged-in user] works"""
        time.sleep(2)
        nose.tools.assert_true(self.home_page.logout_employer)
        time.sleep(3)
        nose.tools.assert_true(
            self.dash_home_page.check_for_new_url(
                self.home_page.PROD_EXIT_PATH_URL+'/employer'
            )
        )




@attr()
# @attr(type="run")
class Test01EmployerForgotPassword(BaseTest):
    """ Test cases for Login Modal - Error Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = "123456"

    @classmethod
    def setUpClass(self):
        super(Test01EmployerForgotPassword, self).setUpClass()
        self.dash_home_page = DashboardHomePage(self._browser)
        self.home_page = EmployerHomePage(self._browser)
        self.prod_employer_page = 'https://www.aasaanjobs.com/employer/'
        self.home_page.go_to(self.prod_employer_page)
        self.home_page.maximize()
        self.email = 'talentacquisition@aasaanjobs.com'

    def test_00_click_login_header(self):
        """00 Test Login Header button works"""
        nose.tools.assert_true(self.home_page.click_login_header)

    def test_01_valid_input_data_using_email(self):
        """01 Test Valid Email for Login Forgot-Password works"""
        nose.tools.assert_true(
            self.home_page.fill_mobile_or_email_id(self.email))

    def test_02_check_forgot_password_link(self):
        """02 Test Forgot Password link appears"""
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)

    def test_03_invalid_fp_email_and_mobile(self):
        """03 Test Invalid Email & Mobile for Forgot-Password works"""
        self.home_page.click_forgot_password_option()

    def test_04_valid_fp_email(self):
        """04 Test Initiate Forgot Password with Valid Email works"""
        nose.tools.assert_true(self.home_page.check_reset_password_success_msg_displayed(self.email))

