# from __future__ import print_function
#
# import nose.plugins.multiprocess
# import nose.tools
# from nose.plugins.attrib import attr
#
# from recruit.testing.page_classes.candidate import *
# from recruit.testing.test_base_class import BaseTest
#
#
# @attr()
# # @attr(type="run")
# class TestProdCandidatePageLoading(BaseTest):
#
#     PROD_URL = "https://www.aasaanjobs.com"
#     HOME_PATH = "https://www.aasaanjobs.com"
#     REGISTER_PATH = "/candidate/register"
#     OTP_VERIFY_PATH = "/employer/emailVerify/notify/"
#
#     _MOBILE = '9820453336'
#     _PASSWORD = '123123'
#
#     @classmethod
#     def setUpClass(self):
#         super(TestProdCandidatePageLoading, self).setUpClass()
#         self.home_page = CandidateHomePage(self._browser)
#         self.dash_homepage = CandidateDashboardHomePage(self._browser)
#         self.matching_jobs = CandidateMatchingJobs(self._browser)
#         self.my_interviews = CandidateInterviewsPage(self._browser)
#         self.add_exp = AddExperiencePage(self._browser)
#         self.applied_history = CandidateAppliedHistoryPage(self._browser)
#         self.search_page = CandidateInternalSearch(self._browser)
#         self.my_resume = MyResumePage(self._browser)
#         self.setting = CandAccountSettingsPage(self._browser)
#         self.home_page._base_url = self.PROD_URL
#         self.home_page.EXIT_PATH_URL = self.PROD_URL
#         self.home_page.go_to_page()
#         self.home_page.maximize()
#
#     def test_00_login_candidate(self):
#         otp_code = self.home_page.get_user_password_otp_prod(self._MOBILE)[1]
#         nose.tools.assert_true(self.home_page.login_user(self._MOBILE, otp_code))
#         time.sleep(7)
#         nose.tools.assert_true(self.matching_jobs.is_current_page)
#
#     def test_01_is_matching_jobs_tab_loading(self):
#         # time.sleep(7)
#         nose.tools.assert_true(self.matching_jobs.is_matching_jobs_title_displayed)
#
#     def test_02_is_application_tab_loading(self):
#         nose.tools.assert_true(self.matching_jobs.check_application_tab_link_works)
#         time.sleep(7)
#         # nose.tools.assert_true(self.my_interviews.is_current_page)
#         nose.tools.assert_true(self.my_interviews.check_application_page_title_is_displayed)
#
#     def test_03_is_home_page_loading(self):
#         nose.tools.assert_true(self.my_interviews.check_home_tab_link_works)
#         time.sleep(5)
#         nose.tools.assert_true(self.dash_homepage.is_current_page)
#         nose.tools.assert_true(self.home_page.check_homepage_title_text_displayed)
#
#     def test_04_check_applied_history_view_more_button_working(self):
#         # self.dash_homepage.go_to_page()
#         nose.tools.assert_true(self.dash_homepage.check_applied_history_view_more_button_working)
#         nose.tools.assert_true(self.my_interviews.check_application_page_title_is_displayed)
#
#     def test_05_check_my_profile_button_working(self):
#         # time.sleep(5)
#         nose.tools.assert_true(self.dash_homepage.click_on_aasaanjobs_logo)
#         time.sleep(3)
#         self.dash_homepage.scroll_to_top()
#         nose.tools.assert_true(self.dash_homepage.click_on_view_profile_button)
#         time.sleep(2)
#         nose.tools.assert_true(self.my_resume.is_current_page)
#         nose.tools.assert_true(self.my_resume.check_default_profile_pic_displayed)
#
#     def test_06_check_search_bar_is_displyed(self):
#         nose.tools.assert_true(self.dash_homepage.click_on_aasaanjobs_logo)
#         time.sleep(3)
#         self.dash_homepage.scroll_to_top()
#         nose.tools.assert_true(self.home_page.check_search_bar_is_displyed)
#
#     def test_07_check_dropdown_my_profile_link_is_working(self):
#         nose.tools.assert_true(self.dash_homepage.check_my_profile_button_works)
#         nose.tools.assert_true(self.my_resume.check_default_profile_pic_displayed)
#
#     def test_08_check_dropdown_setting_link_is_working(self):
#         nose.tools.assert_true(self.applied_history.check_settings_button_works)
#         nose.tools.assert_true(self.setting.check_settings_title_text_displayed)
#
#     def test_09_check_logout_working(self):
#         nose.tools.assert_true(self.setting.logout_candidate)
#
#
#
#
#
#
#
#
