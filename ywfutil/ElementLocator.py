# /usr/bin/python
# encoding:utf-8
from DriverSetup import AndroidTestDriver
from ywfutil.pylog import YwfLog as logger
from ywfutil import getshots


class LocatorController:

    @staticmethod
    def locateElementById(element_id):
        element = None
        try:
            element = AndroidTestDriver.initial().find_element_by_id(element_id)
            return True
        except Exception:
            logger.debug('Element with id %s cannot locate..' % element_id)
            getshots.getScreenShots()
            return False
        finally:
            return element

    @staticmethod
    def locateElementsById(elements_id):
        element_list = None
        try:
            element_list = AndroidTestDriver.initial().find_elements_by_id(elements_id)
            return True
        except Exception:
            logger.debug('Element list with id %s cannot locate..' % elements_id)
            getshots.getScreenShots()
            return False
        finally:
            return element_list

    @staticmethod
    def locateElementByUiAutomator(uiautomator):
        element = None
        try:
            element = AndroidTestDriver.initial().find_element_by_android_uiautomator(uiautomator)
            return True
        except Exception:
            logger.debug('Element with uiautomator %s cannot locate..' % uiautomator)
            getshots.getScreenShots()
            return False
        finally:
            return element

    @staticmethod
    def locateElementsByUiAutomator(uiautomators):
        element_list = None
        try:
            element_list = AndroidTestDriver.initial().find_elements_by_android_uiautomator(uiautomators)
            return True
        except Exception:
            logger.debug('Element list with uiautomator %s cannot locate..' % uiautomators)
            getshots.getScreenShots()
            return False
        finally:
            return element_list

    @staticmethod
    def locateElementByClassName(className):
        element = None
        try:
            element = AndroidTestDriver.initial().find_element_by_class_name(className)
            return True
        except Exception:
            logger.debug('Element with className %s cannot locate..' % className)
            getshots.getScreenShots()
            return False
        finally:
            return element

    @staticmethod
    def locateElementsByClassName(classesName):
        element_list = None
        try:
            element_list = AndroidTestDriver.initial().find_elements_by_class_name(classesName)
            return True
        except Exception:
            logger.debug('Element list with className %s cannot locate..' % classesName)
            getshots.getScreenShots()
            return False
        finally:
            return element_list

    @staticmethod
    def locateElementByName(name):
        element = None
        try:
            element = AndroidTestDriver.initial().find_element_by_name(name)
            return True
        except Exception:
            logger.debug('Element with name %s cannot locate..' % name)
            getshots.getScreenShots()
            return False
        finally:
            return element

    @staticmethod
    def locateElementsByName(names):
        element_list = None
        try:
            element_list = AndroidTestDriver.initial().find_elements_by_name(names)
            return True
        except Exception:
            logger.debug('Element list with name %s cannot locate..' % names)
            getshots.getScreenShots()
            return False
        finally:
            return element_list

    @staticmethod
    def locateElementByXpath(xpath):
        element = None
        try:
            element = AndroidTestDriver.initial().find_element_by_xpath(xpath)
            return True
        except Exception:
            logger.debug('Element with xpath %s cannot locate..' % xpath)
            getshots.getScreenShots()
            return False
        finally:
            return element

    @staticmethod
    def locateElementsByXpath(xpaths):
        element_list = None
        try:
            element_list = AndroidTestDriver.initial().find_elements_by_xpath(xpaths)
            return True
        except Exception:
            logger.debug('Element list with name %s cannot locate..' % xpaths)
            getshots.getScreenShots()
            return False
        finally:
            return element_list
