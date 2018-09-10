# /usr/bin/python
# encoding:utf-8
from ywfutil.ElementLocator import LocatorController
from ywfutil.pylog import YwfLog
from action import ActionController


def lookup_history():
    historyEls = LocatorController.locateElementsById('ad_cover')
    # pageFlag = LocatorController.locateElementById('tv_end_hint')
    pageFlag = False
    loopValue = 0
    if historyEls is True:
        while not pageFlag:
            while loopValue < 3:
                for element in historyEls:
                    element.click()
                    ActionController.delay(2)
                    for actionSwipe in range(0, 3):
                        ActionController.swipe_delta_y(round(2 / 3, 2), round(4 / 5, 2), round(2 / 5, 2))
                        YwfLog.warning(u'执行上滑操作..')
                        ActionController.delay(3)
                    ActionController.swipe_delta_x(round(1 / 5, 2), round(2 / 5, 2), round(3 / 5, 2))
                    YwfLog.warning(u'横滑返回..')
                    ActionController.delay(3)
                ActionController.swipe_delta_y(round(2 / 3, 2), round(4 / 5, 2), round(1 / 4, 2))
                YwfLog.warning(u'浏览列表..')
                ActionController.delay(3)
                loopValue += 1
            if loopValue == 3:
                pageFlag = True
    else:
        YwfLog.warning(u'浏览记录列表为空..')
