from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 首页
        self.browser.get('http://localhost:8000')

        # 页面标题todo
        self.assertIn('To-Do', self.browser.title,"browser title was:" + self.browser.title)
        self.fail('Finish the test!')

        # 输入框

        # 输入

        # 按下回车 更新 显示

        # 又一个框

        # 输入

        # 按下回车 更新 显示

        # 生成url

        # 访问url，看到内容

if __name__ == '__main__':
    unittest.main()




