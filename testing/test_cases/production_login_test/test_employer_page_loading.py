# from __future__ import print_function
#
# import nose.plugins.multiprocess
# import nose.tools
# from nose.plugins.attrib import attr
#
# from recruit.testing.page_classes.employer import *
# from recruit.testing.test_base_class import BaseTest
#
#
# @attr()
# # @attr(type="run")
# class TestProdEmployerPageLoading(BaseTest):
#
#     PROD_URL = "https://www.aasaanjobs.com"
#     HOME_PATH = "/employer"
#     REGISTER_PATH = "/employer/register"
#     EMAIL_VERIFY_PATH = "/employer/emailVerify/notify/"
#     _PASSWORD = '123456'
#     _EMAIL_ID = 'talentacquisition@aasaanjobs.com'
#
#     @classmethod
#     def setUpClass(self):
#         super(TestProdEmployerPageLoading, self).setUpClass()
#         self.er_home_page = EmployerHomePage(self._browser)
#         self.dash_homepage = DashboardHomePage(self._browser)
#         self.my_jobs = MyJobsPage(self._browser)
#         self.my_profile = MyProfilePage(self._browser)
#         self.settings_page = AccountSettingsPage(self._browser)
#         self.my_wallet_page = EmployerMyWalletPage(self._browser)
#         self.er_home_page._base_url = self.PROD_URL
#         self.er_home_page.EXIT_PATH_URL = self.PROD_URL
#         self.er_home_page.go_to_page()
#         self.er_home_page.maximize()
#
#     def test_01_login_employer(self):
#         self.er_home_page.login_user(self._EMAIL_ID, self._PASSWORD)
#
#     def test_03_check_open_tab_is_current_tab(self):
#         nose.tools.assert_true(self.my_jobs.is_open_tab_current_page)
#
#     def test_02_check_draft_tab_is_current_tab(self):
#         nose.tools.assert_true(self.my_jobs.is_draft_tab_current_page)
#
#     def test_04_check_unapproved_tab_is_current_tab(self):
#         nose.tools.assert_true(self.my_jobs.is_unapproved_tab_current_page)
#
#     def test_05_check_closed_tab_is_current_tab(self):
#         nose.tools.assert_true(self.my_jobs.is_closed_tab_current_page)
#
#     def test_06_check_application_tab_is_current_tab(self):
#         nose.tools.assert_true(self.my_jobs.check_application_tab_link_works)
#         nose.tools.assert_true(self.my_jobs.check_filter_or_empty_state_is_present)
#
#     def test_11_check_company_profile_tab_is_current_page(self):
#         nose.tools.assert_true(self.my_jobs.check_company_profile_link_works)
#         nose.tools.assert_true(self.my_profile.is_current_page)
#
#     def test_12_check_settings_is_current_page(self):
#         nose.tools.assert_true(self.my_profile.check_settings_button_works)
#         nose.tools.assert_true(self.settings_page.is_current_page)
#
#     def test_13_check_my_wallet_is_current_page(self):
#         nose.tools.assert_true(self.settings_page.check_my_wallet_tab_works)
#         nose.tools.assert_true(self.my_wallet_page.is_current_page)
