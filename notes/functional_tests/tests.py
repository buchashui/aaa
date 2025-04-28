from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT: 
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 首页
        self.browser.get(self.live_server_url)

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

        self.wait_for_row_in_list_table('1: Buy flowers')

        # 又显示一个文本输入框，可以输入其他待办事项
        # 输入Give a gift to Lisi
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)

        # 页面更新 显示两个待办事项
        self.wait_for_row_in_list_table('1: Buy flowers')
        self.wait_for_row_in_list_table('2: Give a gift to Lisi')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # 用户1
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # 生成唯一的url
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/lists/.+')

        # 用户2
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 看不到用户1的待办事项
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy milk', page_text)

        # 输入新的待办事项
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy eggs')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy eggs')

        # 生成唯一的url
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, '/lists/.+')
        self.assertNotEqual(user1_list_url, user2_list_url)

        # 只有user2的待办事项
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy milk', page_text)
        self.assertIn('Buy eggs', page_text)
        
    def test_layout_and_styling(self):
        # 用户访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 输入框居中显示
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        




