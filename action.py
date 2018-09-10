# /usr/bin/python
# encoding:utf-8
import time
from DriverSetup import AndroidTestDriver

driver = AndroidTestDriver.initial()

class ActionController:
    # 获取屏幕宽度
    @staticmethod
    def getScreenWidth():
        return driver.get_window_size()['width']

    # 获取屏幕高度
    @staticmethod
    def getScreenHeight():
        return driver.get_window_size()['height']

    # 纵向滑动操作，其中x和y的有效值范围为0-1
    @staticmethod
    def swipe_delta_y(origin_x, origin_y, des_y, duration=600):
        if 0 < origin_y < 1 and 0 < des_y < 1 and 0 < origin_x < 1:
            driver.swipe(origin_x * ActionController.getScreenWidth(),
                                     origin_y * ActionController.getScreenHeight(),
                                     origin_x * ActionController.getScreenWidth(),
                                     des_y * ActionController.getScreenHeight(), duration)
            return True
        else:
            return False

    # 横向滑动操作，其中x和y的有效值范围为0-1
    @staticmethod
    def swipe_delta_x(origin_x, origin_y, des_x, duration=600):
        if 0 < origin_x < 1 and 0 < des_x < 1 and 0 < origin_y < 1:
            driver.swipe(origin_x * ActionController.getScreenWidth(),
                                     origin_y * ActionController.getScreenHeight(),
                                     des_x * ActionController.getScreenWidth(),
                                     origin_y * ActionController.getScreenHeight(), duration)
            return True
        else:
            return False

    @staticmethod
    def delay(seconds):
        time.sleep(seconds)

    @staticmethod
    def backForward():
        ActionController.swipe_delta_x(0.25, 0.6, 0.7)
