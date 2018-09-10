import unittest
from DriverSetup import AndroidTestDriver
import time
import component
import mine.minehistory


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = AndroidTestDriver.initial()

    def test_userHistory(self):
        self.driver.find_element_by_id('rl_five_tab').click()
        time.sleep(3)
        self.driver.find_element_by_id(component.mine_module_ids[5]).click()
        time.sleep(4)
        mine.minehistory.lookup_history()
        time.sleep(6)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
