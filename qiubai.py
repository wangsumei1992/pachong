from selenium import webdriver
import time, sys

class Qiubaicontent:

    def __init__(self, pages):
        self.pages = pages
        self.base_url = "https://www.qiushibaike.com/8hr/page/%s"
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def getcontent(self):
        for page in range(1,int(self.pages)+1):
            print("第%s页"%page)
            self.dr.get(self.base_url%page)
            time.sleep(1)
            contents = self.dr.find_elements_by_css_selector(".content>span")
            with open("qiubai.txt", 'w+') as f:
                for i in contents:
                    f.write(i.text)

if __name__ == '__main__':
    pages = sys.argv[1]

    QC = Qiubaicontent(pages)
    QC.getcontent()

