# __author__ = 'tanvijoshi'
"""
_________________________________________________

Test Class for Candidate zone

        Log in function

_________________________________________________
"""
from __future__ import print_function

import nose.tools
import nose.plugins.multiprocess
from nose.plugins.attrib import attr

from recruit.testing.test_base_class import BaseTest
from recruit.testing.page_classes.partner import *
from recruit.testing.page_classes.candidate import *


@attr()
@attr(type="run")
class Test00PartnerLogin(BaseTest):
    """ Test cases for Login Modal - Normal Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = 'dhruvil'
    PROD_URL = "https://www.aasaanjobs.com"

    @classmethod
    def setUpClass(self):
        super(Test00PartnerLogin, self).setUpClass()
        self.home_page = PartnerHomePage(self._browser)
        self.partner_cand_page = MyCandidatesPage(self._browser)
        self.partner_dash_page = PartnerDashboardHome(self._browser)
        self.home_page._base_url = self.PROD_URL
        self.home_page.EXIT_PATH_URL = self.PROD_URL
        # self.dash_home_page = CandidateDashboardHomePage(self._browser)
        # login_details = self.home_page.get_verified_partner_login_detail
        self.home_page.go_to_page()
        self.home_page.maximize()
        self.email = 'tanvijoshi@mailinator.com'
        self.mobile = '9956713311'

    def test_00_check_login_header_button_working(self):
        nose.tools.assert_true(self.home_page.click_login_header)

    # def test_01_invalid_input_data_for_email_or_mobile(self):
    #     self.home_page.fill_invalid_email_and_mobile_values()
    #     nose.tools.assert_true(self.home_page.close_login_model)

    def test_02_valid_input_data_for_email_or_mobile(self):
        self.home_page.go_to_page()
        nose.tools.assert_true(self.home_page.click_login_header)
        # self.home_page.switch_to_login_iframe()
        time.sleep(2)
        self.home_page.fill_mobile_or_email_id(self.email)
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)
        nose.tools.assert_true(self.home_page.check_login_with_mobile_number_link_is_working)
        self.home_page.fill_mobile_or_email_id(self.mobile)
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)

    # def test_03_invalid_input_data_for_password(self):
    #     self.home_page.fill_invalid_password_values()

    def test_04_valid_input_data_for_password(self):
        self.home_page.fill_password_field(self._PASSWORD)
        time.sleep(3)
        res1 = self.partner_dash_page.is_current_page
        # res2 = self.personal_detail_page.is_current_page
        self.assertTrue(res1)

    def test_05_logout_user(self):
        nose.tools.assert_true(self.partner_cand_page.click_on_welcome_modal_close)
        nose.tools.assert_true(self.partner_cand_page.logout_partner)
        time.sleep(3)
        nose.tools.assert_true(self.home_page.is_current_page)


@attr()
# @attr(type="run")
class Test01PartnerForgotPassword(BaseTest):
    """ Test cases for Login Modal - Error Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = '123456'
    PROD_URL = 'https://www.aasaanjobs.com'

    @classmethod
    def setUpClass(self):
        super(Test01PartnerForgotPassword, self).setUpClass()
        self.home_page = PartnerHomePage(self._browser)
        self.partner_cand_page = MyCandidatesPage(self._browser)
        self.partner_basic_detail = OrganizationBasicDetail(self._browser)
        self.home_page._base_url = self.PROD_URL
        self.home_page.EXIT_PATH_URL = self.PROD_URL
        self.home_page.go_to_page()
        self.home_page.maximize()
        # login_details = self.home_page.get_verified_partner_login_detail
        self.email = 'tanvijoshi@mailinator.com'
        self.mobile = '9956713311'

    def test_00_click_login_header(self):
        nose.tools.assert_true(self.home_page.click_login_header)

    def test_01_valid_input_data_using_email(self):
        self.home_page.fill_mobile_or_email_id(self.email)
        time.sleep(2)

    def test_02_check_forgot_password_link(self):
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)
        nose.tools.assert_true(self.home_page.click_forgot_password_option)

    def test_03_valid_fp_email(self):
        self.home_page.check_reset_password_success_msg_displayed(self.email)
        self.home_page.switch_to_page()
        nose.tools.assert_true(self.home_page.close_login_model)
        self.home_page.refresh()

    def test_04_valid_input_data_using_email(self):
        nose.tools.assert_true(self.home_page.click_login_header)
        self.home_page.fill_mobile_or_email_id(self.mobile)
        time.sleep(2)

    def test_05_check_forgot_password_link(self):
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)
