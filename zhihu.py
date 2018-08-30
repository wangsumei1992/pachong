"""从知乎获取每日最热和每月最热"""

from selenium import webdriver
import time

class Zhihu:

    def __init__(self):
        self.base_url = 'https://www.zhihu.com/explore#daily-hot'

    def __enter__(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dr.quit()

    def get_daily_hoturls(self):
        self.dr.get(self.base_url)
        daily_block = self.dr.find_element_by_class_name('tab-panel')
        links = daily_block.find_elements_by_class_name('question_link')
        print(links)
        urls = []
        for i in links:
            urls.append(i.get_attribute('href'))
        return urls

    def get_daily_hots(self):
        result = []
        hot_urls = self.get_daily_hoturls()
        print(hot_urls)
        for url in hot_urls:
            result.append(self.get_answer(url))
        return result

    def get_answer(self, url):
        self.dr.get(url)
        article = {}
        article['title'] = self.dr.find_element_by_css_selector('#QuestionHeader-title').text
        article['author'] = self.dr.find_element_by_css_selector('#AuthorInfo-head > span').text
        article['content'] = self.dr.find_element_by_class_name('RichContent-inner').get_attribute('innerHTML')
        return article

if __name__ == '__main__':
    with Zhihu() as zhihu:
        articles = zhihu.get_daily_hots()
        print(articles)
