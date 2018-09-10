# usr/bin/python
# encoding:utf-8
import os
import subprocess


def __isDeviceConnected():
    try:
        deviceInfo = subprocess.check_output('adb devices').split('\r\n')
        if deviceInfo[1] == '':
            return False
        else:
            return True
    except Exception:
        print('Device connection failed...')


# 动态获取Android版本号
def getAndroidVersion():
    versionObj =  None
    try:
        versionObj = os.popen('adb shell getprop ro.build.version.release')
        versionInfo = versionObj.read().strip('\n')
        return versionInfo
    except Exception:
        print('An unknown error occurred, please check whether you have the permission to access!')
    finally:
        versionObj.close()


# 动态获取Android设备名
def getDeviceName():
    deviceNameObj = None
    try:
        deviceNameObj = os.popen('adb devices')
        deviceName = deviceNameObj.read().replace('\t', '\n').splitlines()[1]
        return deviceName
    except Exception:
        print('An unknown error occurred, please check whether the developer switch is ON!')
    finally:
        deviceNameObj.close()
