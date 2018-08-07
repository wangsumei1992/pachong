from selenium import webdriver
import time

class Novelchaptercontent:

    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get("http://www.xinshubao.net/0/280/")
        self.dr.maximize_window()

    def getnovellist(self):
        chapters = self.dr.find_elements_by_xpath("//div[@id = 'list']/ul/li/a")
        #print(lis)
        result = []
        for chapter in chapters:
            result.append(chapter.get_attribute("href"))
        return result

    def get_content(self):
        for i in self.getnovellist():
            self.dr.get(i)
            time.sleep(2)
            with open("novelcontent.txt", 'w+') as f:
                content = self.dr.find_element_by_id("content")
                f.write(content.text)

if __name__ == '__main__':
    nc = Novelchaptercontent()
    nc.get_content()