import unittest
from time import sleep
import time
from PageObject.login import login_page
from Public.Decorator import setupclass, teardownclass, testcase, teststep
from Public.ReadConfig import ReadConfig

# apk_url = ReadConfig().get_apk_url()
# pkg_name = ReadConfig().get_pkg_name()
# apk_path = ReadConfig().get_apk_path1()
username = ReadConfig().get_testdata('user_name')
pwd = ReadConfig().get_testdata('password')


class testUi(unittest.TestCase, login_page):
    @classmethod
    @setupclass
    def setUpClass(self):
        # self.local_install(apk_path)
        self.d.app_stop_all()
        self.d.app_start("com.vodeapp")

    @classmethod
    @teardownclass
    def tearDownClass(self):
        self.d.app_stop("com.vodeapp")

    """测试我的"""

    @testcase
    @teststep
    def test_01_my(self):
        self.d.xpath('//*[@content-desc="我的, tab, 4 of 4"]').click()
        time.sleep(2)
        self.d.click(0.468, 0.284)
        sleep(3)
        # # 检测 ‘登录/注册’
        self.assertTrue(self.d.xpath(
            '//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))
        self.assertTrue(self.d(text="个人信息"))
        self.assertTrue(self.d(text="商城订单"))
        self.assertTrue(self.d(text="更多订单 "))
        self.assertTrue(self.d(text="待付款"))
        self.assertTrue(self.d(text="待发货"))
        self.assertTrue(self.d(text="待收货"))
        self.assertTrue(self.d(text="已完成"))
        self.assertTrue(self.d(text="退货/换货"))
        self.assertTrue(self.d(text="邀请直播"))
        self.assertTrue(self.d(text="权益中心"))
        self.assertTrue(self.d(text="众筹商品"))
        self.assertTrue(self.d(text="我的红包"))
        self.assertTrue(self.d(text="我的账户"))
        self.assertTrue(self.d(text="客服管理"))
        self.d.swipe(0, 450, 0, 72)
        self.assertTrue(self.d(text="我的项目"))
        self.assertTrue(self.d(text="商城收货地址"))
        self.assertTrue(self.d(text="卡券中心"))
        self.d.swipe(0, 874, 0, 72)
        time.sleep(3)
        self.assertTrue(self.d(text="我的收益"))
        self.assertTrue(self.d(text="活动分享"))
        self.assertTrue(self.d(text="成为会员"))
        self.assertTrue(self.d(text="成为服务商"))
        self.assertTrue(self.d(text="聚合支付"))
        self.assertTrue(self.d(text="素材中心"))
        self.assertTrue(self.d(text="商品收藏"))
        self.assertTrue(self.d(text="历史游览"))
        self.assertTrue(self.d(text="设置"))
        # # 检测 ’商城客服‘
        self.assertTrue(self.d.xpath(
            '//*[@text="商城客服"]'))
        time.sleep(3)

    # """重置密码"""
    # def test_02_resetpwd(self):
    #     self.click_resetpwd_btn()
    #     self.input_username(username[0])
    #     sleep(2)
    #     info = self.get_info()
    #     self.d.press("back")
    #     self.d.press("back")
    #     assert info == True
    #
    # """测试登录"""
    # def test_03_login(self):
    #     self.d.wait_activity('com.yizhuan.cutesound.ui.login.LoginActivity', timeout=10)
    #     sleep(2)
    #     self.input_username(username[0])
    #     self.input_password(pwd[0])
    #     self.click_login_btn()
    #     self.d.wait_activity('com.yizhuan.cutesound.MainActivity', timeout=10)
    #     assert self.d(resourceId='com.wujie.siyu:id/main_home_tab').exists() == True
