# /usr/bin/python
# encoding:utf-8
from ywfutil.ElementLocator import LocatorController
from ywfutil.pylog import YwfLog


def inputText():
    el = LocatorController.locateElementById('et_def_emoticons_text')
    if el is True:
        el.send_keys(u'这是第一条使用自动化脚本输入的文字')
    else:
        YwfLog.warning(u'输入文字框定位失败..')


def shareCommunity():
    communityEl = LocatorController.locateElementById('圈子id')
    if communityEl is True:
        communityEl.click()
    else:
        YwfLog.warning(u'圈子按钮定位失败..')


def atUser():
    atUserEl = LocatorController.locateElementById('atUserElementId')
    if atUserEl is True:
        atUserEl.click()
    else:
        YwfLog.warning(u'@用户定位失败..')


def addMedia():
    pass


def addEmoji():
    pass

# def getWellNumber():
#     pass
