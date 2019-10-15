import unittest
from time import sleep
from selenium import webdriver

class Testbaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.baidu.com"

    def baidu_search(self,search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_search_key_selenium(self):
        search_key = 'selenium'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")

    def test_search_key_unttest(self):
        search_key = 'unittest'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title,search_key+"_百度搜索")