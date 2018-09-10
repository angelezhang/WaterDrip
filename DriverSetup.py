# encoding:utf-8
from appium import webdriver
import adb


class AndroidTestDriver:

    @staticmethod
    def initial():
        desired_caps = {
            'platformName': 'Android',
            'deviceName': adb.getDeviceName(),
            'platformVersion': adb.getAndroidVersion(),
            'appPackage': 'com.feng.car',
            'appActivity': 'com.feng.car.activity.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(15)
        return driver
