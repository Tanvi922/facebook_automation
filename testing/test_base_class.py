
from __future__ import print_function
# import os
import sys
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Test Case Base Class (to be inherited by all Tests)
class BaseTest(unittest.TestCase):
    """ Base test class for all tests """

    TOTAL_TESTS = 0

    @classmethod
    def setUpClass(cls):

        sys.path.append('/usr/local/lib/python3.4/dist-packages/')
        sys.path.append('/home/tanvi/testenv/nayaenv/lib/python3.4')
        sys.path.append('/home/tanvi/testenv/nayaenv/lib/python3.4/site-packages')
        sys.path.append('/usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs')

        cls.start_firefox()



    @classmethod
    def start_firefox(cls):
        """Initialization method to setup a Webdriver instance of Firefox"""

        # #    Setup Local Firefox parameters
        #

        firefox_loc = "/usr/bin/firefox"
        firefox_binary = FirefoxBinary(firefox_loc)
        capability = DesiredCapabilities.FIREFOX.copy()
        #
        capability['loggingPrefs'] = {
            'driver': 'WARNING',
            'server': 'ALL',
            'client': 'ALL',
            'performance': 'ALL',
            'browser': 'SEVERE'}


        cls._browser = webdriver.Firefox(
            firefox_binary=firefox_binary,
            capabilities=capability,
            # firefox_profile=webdriver.FirefoxProfile(), # Experiment with profiles
        )
        cls._browser.set_window_size(1270, 620)
        return cls._browser
    #


    @classmethod
    def tearDownClass(cls):
        """ Here we go, this is where we end it : Tear down the class"""

        with open('browser_console.log', 'w') as log_file:
            # print("\nWe are now going to open and save log data: ")
            for logtype in cls._browser.log_types:
                for log in cls._browser.get_log(logtype):
                    print("\nWe 'ave logs o type : ", log)
                    log_file.write("\n logssss"+str(logtype).capitalize()+" Log : ---\n" + str(log))

        if cls._browser is not None:
            cls._browser.quit()

    def tearDown(self):
        """Cryptic teardown method to analyze test case results"""
        test_name = self._testMethodName
        now = datetime.now()
        print(
            "\n\n",
            # "  << *Test Case Console Output* >>\n",
            " Test Scenario : " + test_name + "\n",
            " >Date _ " + now.strftime("%Y-%m-%d") + "\n",
            " >Time _ " + now.strftime("%I:%M.%f %p") + "\n"
        )
        res = self._outcome
        print("*************before loop", self._browser.get_log('browser'))
        for entry in self._browser.get_log('browser'):
            print("************logs*************", entry)
        for method, error_has_occurred in res.errors:
            if error_has_occurred:
                print("\nFailure Occurred at: \n", method)
                self.take_screenshot_now(label="Failed_")
                self.printMyLogs(label="Failed_")
        with open('browser_log_console.log', 'w') as log_file:
            # print("\nWe are now going to open and save log data: ")
            for logtype in self._browser.log_types:
                for log in self._browser.get_log(logtype):
                    # print("\nWe 'ave logs o type : ", log)
                    log_file.write("\n" + str(logtype).capitalize() + " Log : ---\n" + str(log))
                    for log in self._browser.get_log('browser'):
                        print(log)
                        log_file.write("\n" + str(log).capitalize() + " Log : ---\n" + str(log))
            else:
                pass

    def take_screenshot_now(self, label="Screen_"):
        test_name = self._testMethodName
        test_id = self.id().split(".")
        test_class_title = test_id[len(test_id)-2]
        browser_name = str(self._browser.name)

        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = label + \
            now + "_" +\
            browser_name + "_" + \
            test_class_title + "_" + \
            test_name + \
            ".png"
        self._browser.save_screenshot(screenshot_name)
        return screenshot_name

    def printMyLogs(self, label="Screen_"):
        sampleLogsArray = []
        test_name = self._testMethodName
        test_id = self.id().split(".")
        test_class_title = test_id[len(test_id) - 2]
        browser_name = str(self._browser.name)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        Logs_name = label + \
                          now + "_" + \
                          browser_name + "_" + \
                          test_class_title + "_" + \
                          test_name + \
                          ".log"
        self._browser.get_log(Logs_name)
        for entry in self._browser.get_log('har'):
            print(entry)
            sampleLogsArray.append(entry)
            return sampleLogsArray, Logs_name


    @classmethod
    def get_webdriver(cls):
        if cls._browser is not None:
            return cls._browser
        else:
            print("\nNo web-driver instance found")
