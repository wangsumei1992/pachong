'''获取北京、上海、广州、深圳这几个城市的雾霾指数'''
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.
import time

class Pm25:

    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        base_url = "http://www.pm25.com/%s.html"
        self.urls = []
        for city in ['beijing', 'shanghai', 'guangzhou', 'shenzhen']:
            self.urls.append(base_url %(city))
            #print(self.urls)

    def get_citypm25(self, cityurl):
        self.dr.get(cityurl)
        return {'city': self.by_class_name('bi_loaction_city').text,
                'pm25': self.by_class_name("bi_aqiarea_num").text}

    def get_result(self):
        result = []
        for url in self.urls:
            result.append(self.get_citypm25(url))
            time.sleep(5)
        return result

    def by_class_name(self, classname):
        return self.dr.find_element_by_class_name(classname)

PM = Pm25()
PM.get_result()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# base_url = "http://www.baidu.com"
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# locator = (By.ID, 'kw')
# driver.get(base_url)
#
# WebDriverWait(driver, 10).until(EC.title_is(u'百度一下，你就知道'))
# '''判断title,返回布尔值'''
#
# WebDriverWait(driver, 10).until(EC.title_contains('百度一下'))
# '''判断title,返回布尔值'''
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kw")))
# '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "su")))
# '''判断某个元素是否被加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
#
# WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(by=By.ID, value='kw')))
# '''判断元素是否可见，如果可见就返回这个元素'''

