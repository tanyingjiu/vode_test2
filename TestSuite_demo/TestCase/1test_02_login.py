import unittest
from time import sleep
import time
from PageObject.login import login_page, log
from Public.Decorator import setupclass, teardownclass, testcase, teststep
from Public.ReadConfig import ReadConfig

#
# apk_url = ReadConfig().get_apk_url()
# pkg_name = ReadConfig().get_pkg_name()
# apk_path = ReadConfig().get_apk_path1()
username = ReadConfig().get_testdata('user_name')
pwd = ReadConfig().get_testdata('password')


class testLogin(unittest.TestCase, login_page):

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

    """测试验证‘登录/注册界面’ui"""
    @testcase
    @teststep
    def test_01_login1(self):
        log.i('测试登录/注册ui')
        self.d.xpath('//*[@content-desc="我的, tab, 4 of 4"]').click()
        time.sleep(2)
        self.d.click(0.468, 0.284)
        time.sleep(1)
        self.d.xpath('//*[@text="个人信息"]').click()
        time.sleep(2)
        if self.d(text="手机验证登录"):
            time.sleep(1)
            # self.d(text="").click()
            # self.assertTrue(self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))
            # self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

            # 注册按钮
            self.assertTrue(self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'))
            self.assertTrue(self.d(text="手机验证登录"))
            self.assertTrue(self.d(text="请输入短信验证码"))
            self.assertTrue(self.d.xpath('//android.widget.HorizontalScrollView/android.view.ViewGroup['
                                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '3]/android.view.ViewGroup[ '
                                         '1]'))
            self.assertTrue(self.d(text="其他登陆方式"))
            self.d.swipe(0, 816, 0, 96)
            # 微信登录图标
            self.assertTrue(self.d(text="微信"))
            # 支付宝登录图标
            self.assertTrue(self.d(text="支付宝"))
            #  注册按钮 开始验证注册界面ui
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            time.sleep(1)
            self.assertTrue(self.d(text="请输入手机号"))
            self.assertTrue(self.d(text="请输入短信验证码"))
            # 验证 ‘验证码ui’
            self.assertTrue(self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '3]/android.view.ViewGroup[1]'))
            self.assertTrue(self.d(text="请输入密码"))
            self.assertTrue(self.d(text="注册完成"))
            # 勾选按钮
            self.assertTrue(self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '7]/android.widget.ImageView[1]'))
            self.assertTrue(self.d(text="我已阅读并同意《各有所爱用户协议》"))
            self.assertTrue(self.d(text="其他登陆方式"))
            self.d.drag(0, 816, 0, 96)
            self.assertTrue(self.d(text="微信"))
            self.assertTrue(self.d(text="支付宝"))
            self.d(text="").click()
        else:
            time.sleep(2)
            self.d(text="").click()
            time.sleep(2)
            self.d.swipe(0, 874, 0, 72)
            self.d(text="设置").click()
            time.sleep(1)
            self.d(text="退出登陆").click()
            time.sleep(1)
            self.d(text="确定").click()
            time.sleep(1)
            self.d(text="").click()
            time.sleep(3)
            self.d.xpath('//*[@content-desc="我的, tab, 4 of 4"]').click()
            self.d.click(0.468, 0.284)
            self.d.click(0.468, 0.284)
            time.sleep(2)
            self.assertTrue(self.d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]'))
            self.d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]').click()
            sleep(1)
            # 注册按钮
            self.assertTrue(self.d.xpath(
                '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                '2]/android.view.ViewGroup[1]'))
            self.assertTrue(self.d(text="手机验证登录"))
            self.assertTrue(self.d(text="请输入短信验证码"))
            self.assertTrue(self.d.xpath('//android.widget.HorizontalScrollView/android.view.ViewGroup['
                                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '3]/android.view.ViewGroup[ '
                                         '1]'))
            self.assertTrue(self.d(text="其他登陆方式"))

            # 微信登录图标
            self.d.swipe(0, 816, 0, 96)
            self.assertTrue(self.d(text="微信"))
            # 支付宝登录图标
            self.assertTrue(self.d(text="支付宝"))
            time.sleep(2)
            #  注册按钮 开始验证注册界面ui
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            time.sleep(1)
            self.assertTrue(self.d(text="请输入手机号"))
            self.assertTrue(self.d(text="请输入短信验证码"))
            # 验证 ‘验证码ui’
            self.assertTrue(self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '3]/android.view.ViewGroup[1]'))
            self.assertTrue(self.d(text="请输入密码"))
            self.assertTrue(self.d(text="注册完成"))
            # 勾选按钮
            self.assertTrue(self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                                         '7]/android.widget.ImageView[1]'))
            self.assertTrue(self.d(text="我已阅读并同意《各有所爱用户协议》"))
            self.assertTrue(self.d(text="其他登陆方式"))
            self.d.swipe(0, 816, 0, 96)
            self.assertTrue(self.d(text="微信"))
            self.assertTrue(self.d(text="支付宝"))
            self.d(text="").click()
            print('login ui success')
    """测试登录"""
    @testcase
    @teststep
    def test_02_login(self):
        log.i('测试登录')
        time.sleep(1)
        self.d(text="手机密码登录").click()
        time.sleep(1)
        self.d(text="请输入手机号").click()
        time.sleep(1)
        self.d.xpath('//android.widget.EditText').set_text(username[0])
        self.d(text="请输入密码").click()
        time.sleep(1)
        self.d.xpath('//android.widget.HorizontalScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[2]/android.widget.EditText[1]').set_text(pwd[0])
        self.d.click(0.874, 0.185)
        # 勾选按钮
        self.d.xpath(
            '//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
            '4]/android.widget.ImageView[1]').click()
        # 登录按钮
        self.d.xpath(
            '//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup['
            '1]/android.widget.TextView[1]').click()

    """测试登录之后界面ui"""
    @testcase
    @teststep
    def test_03_login_affter(self):
        log.i('验证登录')
        time.sleep(1)
        self.assertTrue(self.d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
            '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[2]'))
        print('login success')

    """测试购物车ui"""
    @testcase
    @teststep
    def test_04_gouwu(self):
        log.i('购物车')
        time.sleep(3)
        self.d.xpath('//*[@content-desc="购物车, tab, 3 of 4"]').click()
        self.assertTrue(self.d(text="去逛逛"))
        self.assertTrue(self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView['
                                     '1]'))
        print('shopping cart success')

    """测试首页"""
    @testcase
    @teststep
    def test_05_home(self):
        log.i('首页')
        time.sleep(2)
        self.d.xpath('//*[@content-desc="首页, tab, 1 of 4"]/android.view.ViewGroup[1]').click()
        self.assertTrue(self.d(text="呵呵呵的共享商城"))
        self.assertTrue(self.d(text="商城推荐"))
        self.assertTrue(self.d(text="美妆个护"))
        self.assertTrue(self.d(text="生活电器"))
        # 轮播图
        self.assertTrue(self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '2]/android.support.v4.view.ViewPager[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'))
        print('home success')

    """测试购买流程"""
    @testcase
    @teststep
    def test_06_buy_Process(self):
        log.i('购买流程')
        time.sleep(2)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '5]/android.view.ViewGroup[1]/android.widget.TextView[1]').click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d(text="立即购买").click()
        time.sleep(1)
        self.d(text="1支").click()
        self.d(text="确定").click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.widget.ImageView[1]').click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
        time.sleep(2)
        self.assertTrue(self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup['
                                     '2]'))
        self.assertTrue(self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup['
                                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[6]'))
        print('提交订单')
        self.d(resourceId="com.tencent.mm:id/dn").click()
        time.sleep(1)
        self.d(resourceId="com.tencent.mm:id/dm3").click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '2]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d(text="商城首页").click()
        time.sleep(2)
        self.assertTrue(self.d(text="商城推荐"))
        self.assertTrue(self.d(text="美妆个护"))
        self.assertTrue(self.d(text="生活电器"))
        print('回到首页')

