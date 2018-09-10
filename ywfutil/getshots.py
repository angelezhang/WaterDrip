# usr/bin/python
# encoding:utf-8
import time
from DriverSetup import AndroidTestDriver


def getScreenShots():
    screenShotDriver = AndroidTestDriver.initial()
    day = time.strftime('%Y-%M-%D %H-%M-%S', time.localtime(time.time()))
    filePath = '~/Documents/AppScreenShots/%s.png' % day
    while screenShotDriver.session_id is not None:
        screenShotDriver.get_screenshot_as_file(filePath)
        time.sleep(3)
