import unittest
from time import sleep
from PageObject.my_Exercise import my_page1
import time
from PageObject.login import login_page
from Public.Decorator import setupclass, teardownclass, testcase, teststep
from Public.ReadConfig import ReadConfig
from PageObject.vode_news_home import my_other

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

    '''检查测试首页'''
    def test_01_home(self):
        time.sleep(5)
        self.click_home()
        assert self.check_home_Ui() == True

    '''检查消息页面'''
    def test_02_news(self):
        assert self.check_news() == True

    '''检查短视频首页ui'''
    def test_03_short_video_ui(self):
        self.click_home()
        assert self.check_short_video() == True

    '''检查上传短视频'''
    def test_04_upload_video(self):
        self.d.xpath('//*[@text=""]').click()
        assert self.check_upload_video() == True

    '''检查删除视频'''
    def test_05_del_video(self):
        assert self.clear_short_video == True

    '''返回首页'''
    def test_06_home(self):
        self.video_return1_home()

    '''检查智慧店ui'''
    def test_07_wisdom(self):
        assert self.wisdom_shop() == True

    '''检查购买智慧店商品'''
    def test_08_buy_wisdom_shop(self):
        self.shop_home()
        assert self.buy_wisom_shop == True

     '''检查抢红包'''
    def test_09_grab_red(self):
        assert self.check_grab_red() == True

    '''检查试用商品'''
    def test_10_try_goods(self):
        self.d.xpath('//*[@text=""]').click()
        assert self.check_try_goods() == True







