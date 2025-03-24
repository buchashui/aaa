from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 首页
        self.browser.get('http://localhost:8000')

        # 网页标题和头部包含todo
        #self.assertIn('To-Do', self.browser.title,"browser title was:" + self.browser.title)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # 有文本输入框输入待办事项
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 输入Buy flowers
        inputbox.send_keys('Buy flowers')

        # 按下回车，页面更新
        #待办事项表格中显示1：Buy flowers
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn('1: Buy flowers', [row.text for row in rows])

        # 又显示一个文本输入框，可以输入其他待办事项
        # 输入gift to girlfriend
        self.fail('Finish the test!')

        # 输入

        # 按下回车 更新 显示

        # 生成url

        # 访问url，看到内容

if __name__ == '__main__':
    unittest.main()




