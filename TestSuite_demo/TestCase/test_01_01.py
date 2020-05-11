import unittest
from time import sleep
from PageObject.my_Exercise import my_page1
import time
from PageObject.login import login_page
from Public.Decorator import setupclass, teardownclass, testcase, teststep
from Public.ReadConfig import ReadConfig
from PageObject.vode_news_home import my_page1

# apk_url = ReadConfig().get_apk_url()
# pkg_name = ReadConfig().get_pkg_name()
# apk_path = ReadConfig().get_apk_path1()
username = ReadConfig().get_testdata('user_name')
pwd = ReadConfig().get_testdata('password')


class testU(unittest.TestCase, my_page1):

    @classmethod
    @setupclass
    def setUpClass(self):
        self.d.app_stop_all()
        self.d.app_start("com.vodeapp")

    @classmethod
    @teardownclass
    def tearDownClass(self):
        self.d.app_stop("com.vodeapp")

    @testcase
    def test_01(self):
        sleep(5)
        self.click_home()
