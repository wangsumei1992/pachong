import time
from selenium import webdriver

class Dailytopcontent(object):

    def __init__(self):
        self.dr = webdriver.Chrome()

    def topdaily_title_url(self):
        self.dr.get('http://www.qq.com/')
        self.dr.maximize_window()
        time.sleep(5)
        title = self.by_css("#todaytop>a").text
        url = self.by_css("#todaytop>a").get_attribute("href")
        time.sleep(3)
        self.dr.get(url)
        content = self.by_id("articleContent").get_attribute('innerHTML')
        print(title, content)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def by_id(self, id):
        return self.dr.find_element_by_id(id)


if __name__ == '__main__':
    a = Dailytopcontent()
    a.topdaily_title_url()

