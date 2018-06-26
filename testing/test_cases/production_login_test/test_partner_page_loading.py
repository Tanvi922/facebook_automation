# from __future__ import print_function
#
# from nose.plugins.attrib import attr
# from recruit.testing.test_base_class import BaseTest
# from recruit.testing.page_classes.partner import *
#
#
# @attr()
# # @attr(type="run")
# class TestPartnerInternalProduction(BaseTest):
#     """ Test Class for Partner Internal Page Loads """
#
#     _multiprocess_can_split_ = True
#     home_url = "https://www.aasaanjobs.com/partner-zone/home/"
#
#     @classmethod
#     def setUpClass(self):
#         super(TestPartnerInternalProduction, self).setUpClass()
#
#         self.home_page_p = PartnerHomePage(self._browser)
#         self.dash_home = PartnerDashboardHome(self._browser)
#         self.LOGGED_IN = False
#         if True:
#             self.home_page_p.set_prod_config()
#             self.dash_home.set_prod_config()
#         self.home_page_p.go_to_page()
#         self.home_page_p.maximize()
#
#     def test_01_login_verified_partner(self):
#         """ Partner Prod 01 -> Check Login works : """
#         partner_email = self.home_page_p._PARTNER_EMAIL
#         partner_pass = self.home_page_p._PARTNER_PASSWORD
#         self.home_page_p.check_page_element()
#
#         self.home_page_p.login_user(partner_email, partner_pass)
#         self.LOGGED_IN = self.home_page_p.check_for_new_url("partner-zone/home")
#         assert self.dash_home.click_on_warning_modal_close
#         assert self.dash_home.check_cookies()
#         assert self.LOGGED_IN
#
#     def test_02_check_dashboard_todo_link(self):
#         """ Partner Prod 02 -> Check Dashboard pending todo action link works : """
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_dash_todo_link_works()
#         else:
#             assert check_logged_in(self)
#
#     #
#     # def test_03_check_dashboard_link_VAC(self):
#     #
#     # def test_04_check_dashboard_link_REGCAND(self):
#     #
#     # def test_05_check_dashboard_link_IFB(self):
#     #
#     # def test_06_check_dashboard_link_SEL(self):
#     #
#
#     def test_07_check_dashboard_link_ACC(self):
#         """ Partner Prod 07 -> Check Dashboard Account page loads : """
#         self.dash_home.go_to(self.home_url)
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_dash_account_button_works()
#         else:
#             assert check_logged_in(self)
#
#     #
#
#     def test_08_check_navbar_link_CAND(self):
#         """ Partner Prod 08 -> Check Dashboard My Candidate page loads : """
#         self.dash_home.go_to(self.home_url)
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_nav_mycand_button_works()
#             assert self.dash_home.click_on_advanced_cand_page_modal_close
#             assert self.dash_home.close_hopscotch_if_visible()
#         else:
#             assert check_logged_in(self)
#
#     # def test_09_check_navbar_link_CAND_INV(self):
#     #
#     # def test_10_check_navbar_link_CAND_PEND(self):
#     #
#     # def test_11_check_navbar_link_CAND_LEAD(self):
#
#     #
#
#     def test_12_check_navbar_link_VAC(self):
#         """ Partner Prod 12 -> Check Vacancies page loads : """
#         # self.dash_home.click_home()
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_nav_vacancy_button_works()
#         else:
#             assert check_logged_in(self)
#
#     #
#
#     def test_13_check_navbar_link_APPLICTN(self):
#         """ Partner Prod 13 -> Check Applications page loads : """
#         # self.dash_home.click_home()
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_nav_application_button_works()
#         else:
#             assert check_logged_in(self)
#     #
#
#     def test_17_check_navbar_link_ADD_CAND(self):
#         """ Partner Prod 17 -> Check Navbar Add Candidate page loads : """
#         # self.dash_home.click_home()
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_nav_add_candidate_button_works()
#         else:
#             assert check_logged_in(self)
#
#     # def test_18_check_navbar_notification_cta(self):
#     #     self.dash_home.click_home()
#     #     if self.dash_home.check_for_new_url("partner-zone"):
#     #         assert self.dash_home.check_nav_add_candidate_button_works()
#     #     else:
#     #         assert False
#
#     def test_19_check_candidate_detail_page(self):
#         """ Partner Prod 18 -> Check Candidate Detail page loads : """
#         # self.dash_home.click_home()
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_nav_mycand_button_works()
#             assert self.dash_home.click_on_advanced_cand_page_modal_close
#             assert self.dash_home.close_hopscotch_if_visible()
#             assert self.dash_home.check_candidate_detail_link()
#         else:
#             assert check_logged_in(self)
#
#     def test_20_check_job_detail_page(self):
#         """ Partner Prod 19 -> Check Job Detail page loads : """
#         self.dash_home.go_to(self.home_url)
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_nav_vacancy_button_works()
#             # self.take_screenshot_now()
#             assert self.dash_home.check_job_detail_link()
#             # self.take_screenshot_now()
#             self.dash_home.switch_to_old_window()
#             # self.take_screenshot_now()
#         else:
#             assert check_logged_in(self)
#
#     #
#
#     def test_21_check_dropdown_profile_link(self):
#         """ Partner Prod 20 -> Check My Profile page loads : """
#         self.dash_home.go_to(self.home_url)
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_dropdown_profile_button_works()
#         else:
#             assert check_logged_in(self)
#
#     def test_22_check_dropdown_account_link(self):
#         """ Partner Prod 21 -> Check Account Summary page loads : """
#         # self.dash_home.click_home()
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.check_dropdown_account_button_works()
#         else:
#             assert check_logged_in(self)
#
#     def test_23_check_dropdown_logout_link(self):
#         """ Partner Prod 22 -> Check Logout works : """
#         # self.dash_home.click_home()
#         if self.dash_home.check_for_new_url("partner-zone"):
#             # self.take_screenshot_now()
#             assert self.dash_home.logout_partner
#         else:
#             assert check_logged_in(self)
#
#     def tearDown(self):
#         super(TestPartnerInternalProduction, self).tearDown()
#         # print("\nDone with Test >> ", self._testMethodName)
#         # input()
#
#
# def check_logged_in(test_object):
#     """ Utility function to fail elegantly in random error scenarios """
#     print("\nCurrent URL is : ", test_object.get_webdriver().current_url)
#     test_object.take_screenshot_now()
#     test_object.dash_home.print_page_source()
#     return False  # Something is wrong .. why arent we logged-in ?
#
