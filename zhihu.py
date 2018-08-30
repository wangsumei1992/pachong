"""从知乎获取每日最热和每月最热"""

from selenium import webdriver
import datetime

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

class ZhihuReporter:
        def __init__(self):
            self.report_path = path
            self.f = open(path, 'wb')

        def write_header(self):
            self.f.write('<html><head><meta charset="utf-8">')
            self.f.write('<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css">')
            self.f.write('<title>Zhihu Report</title></head>')

        def write_body(self):
            self.f.write('<body>')

        def finish_body(self):
            self.f.write('</body>')

        def write_article(self, articles):
            self.f.write('<h3>知乎%s最热</h3>' %(datetime.date.today().strftime('%Y_%m_%d')))
            for article in articles:

                self.f.write('<div class="container">')
                article_html = '<h3>%s<small>%s</small></h3>' %(article['title'], article['author'])
                article_html += article['content']
                self.f.write(article_html)
                self.f.write('</div>')
                self.f.write('<hr>')

        def finish_report(self):
            self.finish_body()
            self.f.write('</html>')
            self.f.close()

        def build_article_report(self, articles):
            self.write_header()
            self.write_body()
            self.write_article()
            self.finish_report()


if __name__ == '__main__':
    with Zhihu() as zhihu:
        articles = zhihu.get_daily_hots()
        report_name = 'zhihu_%s.html' % (datetime.date.today().strftime('%Y_%m_%d'))
        reporter = ZhihuReporter(report_name)
        reporter.build_article_report(articles)
