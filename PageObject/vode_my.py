import random
from time import sleep

from Public.Decorator import *

from appium import webdriver

import keyword


class my_page1(BasePage):

    @teststep
    def click_my1(self):
        log.i('点击我的')
        self.d.implicitly_wait(20)
        self.d.xpath('//*[@content-desc="我的, tab, 4 of 4"]').click()

    @teststep
    def return_button(self):
        log.i('返回上一页')
        self.d.implicitly_wait(10)
        self.d.xpath('//*[@text=""]').click()

    @teststep
    def slide_bottom(self):
        log.i('滑动到底部')
        time.sleep(2)
        self.d.swipe(0, 874, 0, 72)

    @teststep
    def slide_half(self):
        log.i('微微滑动')
        time.sleep(2)
        self.d.swipe(0, 400, 0, 72)


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
    def check_sever(self):
        log.i('检查会员图标')
        if self.d.xpath('//*[@text="SAVER会员"]').exists:
            return True
        else:
            return False

    @teststep
    def check_lianxi(self):
        log.i('检查联系店主')
        if self.d.xpath('//*[@text="联系店主"]').exists:
            return True
        else:
            return False

    @teststep
    def check_order(self):
        log.i('检查商城订单')
        self.d.xpath('//*[@text="商城订单"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="商城订单"]') and \
                self.d.xpath('//*[@text="全部"]') and \
                self.d.xpath('//*[@text="待付款"]') and \
                self.d.xpath('//*[@text="待发货"]') and \
                self.d.xpath('//*[@text="待收货"]') and \
                self.d.xpath('//*[@text="已完成"]').exists:
            return True
        else:
            return False

    @teststep
    def check_search_order(self):
        log.i('检查搜索订单')
        self.d.xpath('//*[@text="商城订单"]').click()
        time.sleep(1)
        self.d.xpath(
            '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
            '1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        self.d(text="搜索我的订单").send_keys('美肌')
        self.d.set_fastinput_ime(False)
        time.sleep(3)
        self.d.click(0.907, 0.957)
        time.sleep(2)
        if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '2]/android.view.ViewGroup[2]/android.widget.ScrollView[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]'):
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]').click()
            return True
        else:
            return False

    @teststep
    def check_invite_live(self):
        log.i('检查邀请直播')
        self.d(text="邀请直播").click()
        time.sleep(1)
        if self.d(text="我是服务商") and self.d(text="我是主播").exists:
            return True


    @teststep
    def check_zc_goods(self):
        log.i('检查众筹商品')
        self.d.xpath('//*[@text="众筹商品"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="众筹商品"]') and self.d.xpath('//*[@text="进行中"]') and self.d.xpath(
                '//*[@text="众筹成功"]') and self.d.xpath('//*[@text="众筹失败"]').exists:
            return True
        else:
            return False

    @teststep
    def check_Red_envelope(self):
        log.i('检查我的红包')
        self.d.xpath('//*[@text="我的红包"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="我的红包"]') and self.d.xpath('//*[@text="免单列表"]') and self.d.xpath(
                '//*[@text="抢到的红包"]').exists:
            return True
        else:
            return False

    @teststep
    def check_envelope_details(self):
        log.i('检查红包详情')
        self.d.xpath('//*[@text="我的红包"]').click()
        time.sleep(1)
        # 点击进入红包详情
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.support.v4.view.ViewPager['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.support.v4.view.ViewPager['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="红包详情"]') and self.d.xpath('//*[@text="提现"]') and self.d.xpath(
                '//*[@text="首页"]') and self.d.xpath('//*[@text="分享"]').exists:
            return True
        else:
            return False

    @teststep
    def check_envelope_details1(self):
        log.i('抢到的红包详情')
        self.d.xpath('//*[@text="我的红包"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="抢到的红包"]').click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.support.v4.view.ViewPager['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.support.v4.view.ViewPager['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="已抢"]') and self.d.xpath('//*[@text="呵呵呵"]') and \
                self.d.xpath('//*[@text="￥0.02"]').exists:
            return True
        else:
            return False

    @teststep
    def check_my_account_ui(self):
        log.i('检查我的账户')
        self.d(text="我的账户").click()
        if self.d(text="用户账户") and self.d(text="主播账户") and self.d(text="充值") and self.d(text="账单记录") and self.d(text="我的账户"):
            self.d(text="").click()
            return True

    @teststep
    def check_account_top_up(self):
        log.i('检查我的账户-充值')
        self.d(text="我的账户").click()
        self.d(text="充值").click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
        self.d(text="微信支付").click()
        time.sleep(2)
        if self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[6]'):
            self.d(resourceId="com.tencent.mm:id/dn").click()
            self.d(resourceId="com.tencent.mm:id/dm3").click()
            self.d(text="").click()
            self.d(text="").click()
            return True

    @teststep
    def check_kf_live(self):
        log.i('检查客服管理')
        self.d(text="客服管理").click()
        if self.d.xpath('//*[@resource-id="com.vodeapp:id/action_bar_root"]/android.widget.FrameLayout['
                        '1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[1]/android.widget.TextView[1]'):
            self.d(text="").click()
            return True


    @teststep
    def check_my_project(self):
        log.i('检查我的项目')
        self.d.xpath('//*[@text="我的项目"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="我的项目"]') and self.d.xpath('//*[@text="未进行"]') and self.d.xpath('//*[@text="已完成"]') \
                and self.d.xpath('//*[@text="已过期"]') and self.d.xpath('//*[@text="进行中"]').exists:
            return True
        else:
            return False

    @teststep
    def check_shop_address(self):
        log.i('检查添加商城收货地址')
        self.d.xpath('//*[@text="商城收货地址"]').click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]').click()

        if self.d.xpath('//*[@text="添加新地址"]'):
            self.d.xpath('//*[@text=""]').click()
            time.sleep(1)
            self.d.xpath('//*[@text="确认"]').click()
            time.sleep(1)
            self.d.xpath('//*[@text=""]').click()
            return True
    @teststep
    def check_Coupon_Center(self):
        log.i('检查卡券中心')
        self.d.xpath('//*[@text="卡券中心"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="卡券中心"]') and self.d.xpath('//*[@text="我的卡券"]') and self.d.xpath('//*[@text="共10'
                                                                                                    '张价值100元"]') and \
                self.d.xpath('//*[@text="现金券"]') and self.d.xpath('//*[@text="立即领取"]').exists:
            return True


    @teststep
    def check_myuser_income(self):
        log.i('检查我的收益--我是用户')
        self.d.xpath('//*[@text="我的收益"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="我是用户"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="我的收益"]') and self.d.xpath('//*[@text="可提现"]') and self.d.xpath('//*[@text="待提现"]') and self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]'):
            self.d.xpath('//*[@text="提现"]').click()
            time.sleep(1)
            self.d.xpath('//*[@resource-id="android:id/button1"]').click()
            time.sleep(1)
            if self.d.xpath('//*[@text="实名认证"]') and self.d.xpath('//*[@text="提交"]'):
                return True
            return True
    @teststep
    def check_mysever_income(self):
        log.i('检查我的收益-会员')
        self.d.xpath('//*[@text="我的收益"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="SAVER会员"]').click()
        time.sleep(1)
        if self.d.xpath('//*[@text="我的收益"]'):
            self.d.xpath('//*[@text="提现明细"]').click()
            time.sleep(1)
            if self.d.xpath('//*[@text="提现明细"]') and self.d.xpath('//*[@text="全部"]').exists:
                return True
        return True


    @teststep
    def check_share_activity(self):
        log.i('检查活动分享')
        self.d.xpath('//*[@text="活动分享"]').click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '2]/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView[1]').click()
        if self.d.xpath('//*[@text="微信好友"]') and self.d.xpath('//*[@text="朋友圈"]'):
            self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
            self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
            time.sleep(1)
            self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                         '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()
            if self.d.xpath('//*[@text="微信好友"]') and self.d.xpath('//*[@text="微信好友"]'):
                self.d.xpath( '//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                              '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                              '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
                return True
        return True

    @teststep
    def check_saver_buy_kucun(self):
        log.i('检查会员入口-库存管理-买库存')
        self.d.xpath('//*[@text="SAVER会员"]').click()
        self.d.xpath('//*[@text="库存管理/线下实体端口"]').click()
        time.sleep(2)
        time.sleep(1)
        self.d.xpath('//*[@text="自己购买库存"]').click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]').click()
        time.sleep(1)
        self.d(text="请输入您的姓名").send_keys('测试姓名')
        self.d(text="请输入您的手机号码").send_keys('15975003487')
        self.d.set_fastinput_ime(False)
        self.d.click(0.552, 0.366)
        self.d.click(0.552, 0.366)
        time.sleep(1)
        self.d.xpath('//*[@text="北京"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="朝阳区"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="三环以内"]').click()
        time.sleep(1)
        self.d(text="街道、楼牌号等").send_keys('address')
        time.sleep(2)
        self.d.click(0.829, 0.132)
        time.sleep(2)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[3]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        self.d.swipe(0, 874, 0, 72)
        time.sleep(2)
        self.d.xpath('//*[@text="确定支付"]').click()
        time.sleep(3)
        self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.widget.ImageView[1]').click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').click()
        time.sleep(5)
        if self.d.xpath('//*[@resource-id="com.tencent.mm:id/b17"]/android.view.ViewGroup[1]/android.view.ViewGroup['
                        '1]/android.view.ViewGroup[3]/android.view.ViewGroup[2]'):
            self.d.xpath('//*[@resource-id="com.tencent.mm:id/dn"]').click()
            self.d.xpath('//*[@resource-id="com.tencent.mm:id/dm3"]').click()
            return True

    @teststep
    def check_saver_transfer_kucun(self):
        log.i('检查会员入口-库存管理-划拨库存')
        self.d.xpath('//*[@text="SAVER会员"]').click()
        self.d.xpath('//*[@text="库存管理/线下实体端口"]').click()
        time.sleep(2)
        self.d(text="给好友划拨库存").click()
        time.sleep(1)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.widget.ScrollView[1]/android.view.ViewGroup[1]/android.view.ViewGroup[4]').click()
        time.sleep(1)
        self.d(text="请输入好友的姓名").send_keys('测试姓名')
        self.d(text="请输入好友的手机号码").send_keys('15975003489')
        self.d.click(0.568, 0.371)
        self.d.click(0.568, 0.371)
        self.d.xpath('//*[@text="北京"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="朝阳区"]').click()
        time.sleep(1)
        self.d.xpath('//*[@text="三环以内"]').click()
        time.sleep(1)
        self.d(text="街道、楼牌号等").send_keys('address')
        time.sleep(2)
        self.d.swipe(0, 874, 0, 72)
        time.sleep(2)
        self.d(text="获取验证码").click()
        time.sleep(1)
        self.d(text="请输入短信验证码").send_keys('111111')
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[4]/android.widget.ScrollView[1]/android.view.ViewGroup['
                     '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]').click()
        self.d(text="支付并授权").click()
        time.sleep(1)
        if self.d(text="订单支付").exists():
            return True

    @teststep
    def check_sever_promote(self):
        log.i('检查会员入口推广图片')
        self.d.xpath('//*[@text="SAVER会员"]').click()
        time.sleep(1)
        self.d(text="推广图片").click()
        if self.d(text="推广图片") and self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                                                '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                '1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                                                '1]/android.widget.ScrollView[1]/android.view.ViewGroup['
                                                '1]/android.view.ViewGroup[1]/android.widget.ScrollView['
                                                '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]') and self.d(
            text="商户编码：165193"):
            self.d.swipe(0, 874, 0, 72)
            time.sleep(1)
            self.d(text="保存图片分享给好友").click()
            time.sleep(1)
            self.d(text="保存到手机相册").click()
            time.sleep(2)
            if self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup['
                            '1]/android.view.ViewGroup[1]'):
                return True
        time.sleep(2)

    @teststep
    def check_envelope(self):
        log.i('检查会员入口-红包管理')
        self.d.xpath('//*[@text="SAVER会员"]').click()
        time.sleep(1)
        self.d(text="红包管理").click()
        time.sleep(1)
        if self.d(text="回馈给推荐者和购买者的红包比例设置:").exists():
            return True

    @teststep
    def check_sever_home(self):
        log.i('检查会员入口-我是服务商整个ui')
        self.d.xpath('//*[@text="SAVER会员"]').click()
        time.sleep(1)
        if self.d(text="增值云店") and self.d(text="我的收益") and self.d(text="我的授权人") and self.d(text="我的好友") and self.d(text="店主推荐").exists:
            return True

    def check_material(self):
        log.i('检查素材中心')
        self.d(text="素材中心").click()
        time.sleep(1)
        if self.d(text="素材中心").exists():
            return True

    @teststep
    def check_collect(self):
        log.i('检查商品收藏')
        self.d(text="商品收藏").click()
        time.sleep(1)
        if self.d(text="商品收藏").exists():
            return True

    @teststep
    def check_history_record(self):
        log.i('检查历史预览')
        self.d(text="历史游览").click()
        time.sleep(1)
        if self.d(text="历史游览").exists():
            return True

    @teststep
    def check_set_modify(self):
        log.i('检查设置--修改密码')
        self.d(text="设置").click()
        time.sleep(1)
        self.d(text="修改密码").click()
        time.sleep(1)
        self.d(text="请输入旧密码").send_keys('qwer1234')
        self.d(text="请输入新密码").send_keys('qwer1234')
        self.d(text="再次确认密码").send_keys('qwer1234')
        time.sleep(1)
        self.d(text="确定修改").click()
        time.sleep(2)
        if self.d(resourceId="android:id/scrollView"):
            self.d(resourceId="android:id/button1").click()
            return True

    @teststep
    def check_set_up_ui(self):
        log.i('检查设置里面的ui')
        self.d(text="设置").click()
        time.sleep(1)
        if self.d(text="微信") and self.d(text="支付宝") and self.d(text="常见问题") and self.d(text="意见反馈") and\
                self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup['
                             '2]/android.view.ViewGroup[6]') and self.d(text="清除缓存") and\
                self.d(text="隐私保护指引").exists():
            return True

    @teststep
    def check_zhengjianID(self):
        log.i('检查证件信息')
        self.d(text="设置").click()
        time.sleep(1)
        self.d(text="证照信息").click()
        if self.d(text="广东各有所爱信息科技有限公司") and self.d.xpath('//android.widget.ScrollView/android.view.ViewGroup[1]').exists:
            return True




















