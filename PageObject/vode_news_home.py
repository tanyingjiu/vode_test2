import random
from time import sleep

from Public.Decorator import *

from appium import webdriver

import keyword


class my_other(BasePage):

    @teststep
    def check_news(self):
        log.i('检查消息')
        self.d.xpath('//*[@content-desc="消息, tab, 2 of 4"]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        if self.d(text="社交消息") and self.d(text="短视频消息") and self.d(text="商城消息").exists():
            return True

    @teststep
    def click_home(self):
        log.i('点击首页')
        self.d.xpath('//*[@content-desc="首页, tab, 1 of 4"]/android.view.ViewGroup[1]').click()
        time.sleep(1)

    @teststep
    def shop_home(self):
        log.i('返回商城首页')
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '2]/android.view.ViewGroup[1]').click()
        time.sleep(2)
        self.d.xpath('//*[@text="商城首页"]').click()

    @teststep
    def check_home_Ui(self):
        log.i('检查首页ui')
        time.sleep(1)
        if self.d(text="短视频") and self.d(text="智慧商店") and \
                self.d(text="智慧商店") and \
                self.d(text="超值排行") and \
                self.d(text="抢红包") and \
                self.d(text="每日上新") and \
                self.d(text="美肌优选") and \
                self.d(text="免费试用") and self.d(text="生活必买").exists():
            return True

    @teststep
    def check_short_video(self):
        log.i('检查短视频-进入画面-验证头像-点赞-评论-转发-ui')
        self.d(text="短视频").click()
        time.sleep(1)
        if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[2]') and \
                self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup['
                             '3]/android.widget.ImageView[1]') and \
                self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup['
                             '4]/android.widget.ImageView[1]') and \
                self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup['
                             '5]/android.widget.ImageView[1]') and \
                self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[1]') and \
                self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                             '2]/android.widget.ImageView[1]') and \
                self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[6]').exists:
            return True

    @teststep
    def check_upload_video(self):
        log.i('检查上传视频')
        self.d(text="短视频").click()
        time.sleep(1)
        self.d.xpath('//*[@content-desc="SVAddPage, tab, 3 of 5"]/android.widget.ImageView[1]').click()
        time.sleep(1)
        self.d(resourceId="com.vodeapp:id/chose_local_video_text").click()
        time.sleep(1)
        self.d(scrollable=True).scroll.toEnd()
        time.sleep(2)
        self.d.xpath('//*[@resource-id="com.android.gallery3d:id/list_albumset"]/android.widget.FrameLayout['
                     '5]/android.widget.RelativeLayout[1]').click()
        time.sleep(1)
        self.d.click(0.381, 0.324)
        time.sleep(2)
        self.d(resourceId="com.android.gallery3d:id/head_select_right").click()
        time.sleep(1)
        self.d(resourceId="com.vodeapp:id/btn_next").click()
        time.sleep(1)
        self.d(resourceId="com.vodeapp:id/btn_complete").wait(timeout=5).click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]').wait(
            timeout=20)
        self.d(text="请输入标题").send_keys('test')
        time.sleep(1)
        self.d(text="选择商品").click()
        time.sleep(1)
        self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '2]/android.widget.ImageView[1]').click()
        self.d(text="确定").click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                     '1]/android.widget.TextView[1]').click()
        time.sleep(5)
        if self.d(resourceId="android:id/alertTitle"):
            self.d(resourceId="android:id/button1").click()
            if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                            '4]/android.view.ViewGroup[1]').exists:
                return True

    @teststep
    def clear_short_video(self):
        log.i('清除短视频环境')
        self.d(text="短视频").click()
        time.sleep(1)
        self.d.xpath(
            '//*[@content-desc="SVMyPage, tab, 5 of 5"]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup[1]'):
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                         '4]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
            time.sleep(1)
            self.d(resourceId="android:id/button1").click()
        else:
            return False

    @teststep
    def video_return1_home(self):
        log.i('短视频返回首页')
        self.d.xpath('//*[@content-desc="SVHomePage, tab, 1 of 5"]/android.view.ViewGroup['
                     '1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

    @teststep
    def search_short_video(self):
        log.i('检查短视频搜索')
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup['
                     '1]/android.widget.ImageView[1]').click()
        time.sleep(1)
        self.d(text="热门搜索").send_keys('美肌')
        time.sleep(1)
        self.d.click(0.907, 0.957)
        if self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.widget.ImageView[1]'):
            return True
        self.d(text="").click()

    @teststep
    def wisdom_shop(self):
        log.i('检查智慧商店ui')
        self.d(text="智慧商店").click()
        time.sleep(1)
        if self.d(text="线下好店") and \
                self.d.xpath(
                    '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]') and \
                self.d(text="好店推荐").exists:
            return True

    @teststep
    def buy_wisom_shop(self):
        log.i('检查购买线下店商品')
        self.d(text="智慧商店").click()
        time.sleep(1)
        self.d.xpath('//android.support.v4.view.ViewPager/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]').click()
        time.sleep(2)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView['
                     '1]/android.view.ViewGroup[1]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d(text="立即购买").click()
        time.sleep(1)
        self.d(text="1瓶").click()
        time.sleep(1)
        self.d(resourceId="com.huawei.camera:id/shutter_button").click()
        time.sleep(1)
        # 判断会员立减价格
        if self.d(text="付款: ￥39.00"):
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
            time.sleep(1)
            # 勾选微信支付
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ScrollView['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
            time.sleep(1)
            # 调取支付
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
            time.sleep(5)
            if self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]') and \
                    self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup['
                                 '1]/android.view.ViewGroup[1]/android.view.ViewGroup[6]'):
                self.d(resourceId="com.tencent.mm:id/dn").click()
                time.sleep(1)
                self.d(resourceId="com.tencent.mm:id/dm3").click()
                time.sleep(2)
                self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
                time.sleep(1)
                self.d(text="商城首页").click()
                return True

    @teststep
    def check_grab_red(self):
        log.i('检查抢红包')
        self.d(text="抢红包").click()
        time.sleep(1)
        if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView[1]'):
            self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
            if self.d(text="红包详情") and self.d.xpath('//*[@resource-id="android:id/content"]/android.widget'
                                                    '.FrameLayout[1]/android.view.ViewGroup['
                                                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                    '1]/android.view.ViewGroup[1]/android.view.ViewGroup[5]').exists:
                return True

    @teststep
    def check_try_goods(self):
        log.i('检查试用商品')
        self.d(text="免费试用").click()
        time.sleep(1)
        self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
        time.sleep(1)
        self.d(text="立即体验").click()
        time.sleep(1)
        self.d(text="男款").click()
        time.sleep(1)
        self.d(text="确定").click()
        time.sleep(1)
        # 提交订单
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        time.sleep(3)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
        if self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]') and self.d.xpath('//*[''@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[6]'):
            self.d(resourceId="com.tencent.mm:id/dn").click()
            time.sleep(1)
            self.d(resourceId="com.tencent.mm:id/dm3").click()
            time.sleep(2)
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            time.sleep(1)
            self.d(text="商城首页").click()
            return True
        else:
            return True
















