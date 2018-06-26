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
from recruit.testing.page_classes.candidate import *


@attr()
# @attr(type="run")
class Test00CandidateLoginMobilePassword(BaseTest):
    """ Test cases for Login Modal - Normal Flow"""

    _multiprocess_can_split_ = True
    mobile = '8080255053'
    email = 'tanvijoshi922@gmail.com'
    _PASSWORD = '123456'
    PROD_URL = "https://www.aasaanjobs.com"

    @classmethod
    def setUpClass(self):
        super(Test00CandidateLoginMobilePassword, self).setUpClass()
        self.home_page = CandidateHomePage(self._browser)
        self.personal_detail_page = CandidatePersonalDetailsPage(self._browser)
        self.dash_home_page = CandidateDashboardHomePage(self._browser)
        self.matching_jobs_page = CandidateMatchingJobs(self._browser)
        self.home_page._base_url = self.PROD_URL
        self.home_page.EXIT_PATH_URL = self.PROD_URL
        self.home_page.go_to_page()
        self.home_page.maximize()
        login_details = self.home_page.get_one_time_logged_in_candidate
        # self.email = login_details[0]
        self.mobile = '8080255053'

    def test_00_check_login_header_button_working(self):
        nose.tools.assert_true(self.home_page.click_login_header)

    def test_01_check_facebook_login_working(self):
        nose.tools.assert_true(self.home_page.click_on_facebook_login)
        self.home_page.click_on_back_button()

    def test_02_check_google_login_working(self):
        nose.tools.assert_true(self.home_page.click_login_header)
        nose.tools.assert_true(self.home_page.click_on_google_login)

    def test_03_check_linkedin_login_working(self):
        nose.tools.assert_true(self.home_page.click_login_header)
        nose.tools.assert_true(self.home_page.click_on_linkedin_login)
        self.home_page.click_on_back_button()

    def test_04_invalid_input_data_for_mobile(self):
        nose.tools.assert_true(self.home_page.click_login_header)
        # self.home_page.fill_invalid_mobile_values()

    def test_05_valid_input_data_for_mobile(self):
        self.home_page.fill_mobile_number(self.mobile)
        nose.tools.assert_true(self.home_page.click_login_with_password_option)
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)

    def test_06_valid_input_data_for_password(self):
        self.home_page.fill_password_field(self._PASSWORD)
        time.sleep(3)
        res1 = self.matching_jobs_page.is_current_page
        self.assertTrue(res1)

    def test_07_logout_user(self):
        nose.tools.assert_true(self.home_page.logout_candidate)
        time.sleep(3)
        nose.tools.assert_true(self.home_page.is_current_page)


@attr()
# @attr(type="run")
class Test01CandidateForgotPasswordMobile(BaseTest):
    """ Test cases for Login Modal - Error Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = '123456'
    PROD_URL = "https://www.aasaanjobs.com"
    mobile_no = '8080255053'

    @classmethod
    def setUpClass(self):
        super(Test01CandidateForgotPasswordMobile, self).setUpClass()
        self.home_page = CandidateHomePage(self._browser)
        self.personal_detail_page = CandidatePersonalDetailsPage(self._browser)
        self.dash_home_page = CandidateDashboardHomePage(self._browser)
        self.matching_jobs_page = CandidateMatchingJobs(self._browser)
        self.home_page._base_url = self.PROD_URL
        self.home_page.EXIT_PATH_URL = self.PROD_URL
        self.home_page.go_to_page()
        self.home_page.maximize()
        login_details = self.home_page.get_one_time_logged_in_candidate
        # self.email = login_details[0]
        self.mobile = login_details

    def test_00_click_login_header(self):
        nose.tools.assert_true(self.home_page.click_login_header)

    def test_01_valid_input_data_using_number(self):
        self.home_page.fill_mobile_number(self.mobile_no)
        # time.sleep(2)

    def test_02_check_forgot_password_link(self):
        nose.tools.assert_true(self.home_page.click_login_with_password_option)
        nose.tools.assert_true(self.home_page.is_forgot_password_option_displayed)
        nose.tools.assert_true(self.home_page.click_forgot_password_option)

    def test_03_check_resend_reset_otp_link_working(self):
        # self.home_page.fill_forgot_password_mobile_or_email_field(self.mobile)
        nose.tools.assert_true(self.home_page.click_resend_forgot_password_otp_link)
        self.home_page.check_resend_forgot_password_otp_link_working()

    def test_04_click_on_login_with_otp_button(self):
        nose.tools.assert_true(self.home_page.click_on_forgot_password_login_with_otp_button)

    def test_05_enter_correct_otp_and_password(self):
        time.sleep(3)
        otp_code = self.home_page.get_user_password_otp_prod(self.mobile_no)[2]
        self.home_page.fill_otp_field(otp_code)

    def test_06_valid_input_data_for_password(self):
        self.home_page.fill_password_field(self._PASSWORD)
        time.sleep(3)
        res1 = self.matching_jobs_page.is_current_page
        self.assertTrue(res1)

    def test_07_logout_user(self):
        time.sleep(2)
        nose.tools.assert_true(self.home_page.logout_candidate)
        time.sleep(5)
        nose.tools.assert_true(self.home_page.is_current_page)


@attr()
# @attr(type="run")
class Test02CandidateLoginEmail(BaseTest):
    """ Test cases for Login Modal - Error Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = '123456'
    PROD_URL = "https://www.aasaanjobs.com"
    mobile_no = '8080255053'
    email = 'tanvijoshi922@gmail.com'

    @classmethod
    def setUpClass(self):
        super(Test02CandidateLoginEmail, self).setUpClass()
        self.home_page = CandidateHomePage(self._browser)
        self.personal_detail_page = CandidatePersonalDetailsPage(self._browser)
        self.dash_home_page = CandidateDashboardHomePage(self._browser)
        self.matching_jobs_page = CandidateMatchingJobs(self._browser)
        self.verify_cand_page = VerifyCandidatePage(self._browser)
        self.home_page._base_url = self.PROD_URL
        self.home_page.EXIT_PATH_URL = self.PROD_URL
        self.home_page.go_to_page()
        self.home_page.maximize()
        login_details = self.home_page.get_one_time_logged_in_candidate
        # self.email = login_details[0]
        self.mobile = login_details

    def test_00_click_on_login_button(self):
        nose.tools.assert_true(self.home_page.click_login_header)

    def test_01_valid_input_data_for_email(self):
        self.home_page.fill_mobile_number(self.email)
        nose.tools.assert_true(self.home_page.is_email_forgot_password_option_displayed)

    def test_03_valid_input_data_for_password(self):
        self.home_page.fill_password_field(self._PASSWORD)
        time.sleep(3)
        res1 = self.verify_cand_page.is_current_page
        nose.tools.assert_true(res1)

    def test_04_logout_user(self):
        nose.tools.assert_true(self.home_page.logout_candidate)
        time.sleep(3)
        nose.tools.assert_true(self.home_page.is_current_page)


@attr()
# @attr(type="run")
class Test03CandidateForgotPasswordEmail(BaseTest):
    """ Test cases for Login Modal - Error Flow"""

    _multiprocess_can_split_ = True
    _PASSWORD = '123456'
    PROD_URL = "https://www.aasaanjobs.com"
    mobile_no = '8080255053'
    email = 'tanvijoshi922@gmail.com'

    @classmethod
    def setUpClass(self):
        super(Test03CandidateForgotPasswordEmail, self).setUpClass()
        self.home_page = CandidateHomePage(self._browser)
        self.personal_detail_page = CandidatePersonalDetailsPage(self._browser)
        self.dash_home_page = CandidateDashboardHomePage(self._browser)
        self.matching_jobs_page = CandidateMatchingJobs(self._browser)
        self.home_page._base_url = self.PROD_URL
        self.home_page.EXIT_PATH_URL = self.PROD_URL
        self.home_page.go_to_page()
        self.home_page.maximize()
        login_details = self.home_page.get_one_time_logged_in_candidate
        self.mobile = login_details

    def test_12_valid_fp_email(self):
        nose.tools.assert_true(self.home_page.click_login_header)
        self.home_page.fill_mobile_number(self.email)
        nose.tools.assert_true(self.home_page.click_email_forgot_password_option_displayed)
        self.home_page.check_reset_password_success_msg_displayed()
        # self.home_page.switch_to_page()
        nose.tools.assert_true(self.home_page.close_login_model)
        self.home_page.refresh()
