'''获取豆瓣正在热映电影和读书中的内容'''
from selenium import webdriver
import time

class Douban(object):

    def __init__(self):
        self.book_url = 'https://book.douban.com'
        self.movie_url = 'https://movie.douban.com/cinema/nowplaying/beijing/'

    def __enter__(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.dr.quit()

    def get_nowplaying_movies(self):
        def by_rate(dic):
            return float(dic['rate'])
        self.dr.get(self.movie_url)
        dir_wrap = self.dr.find_element_by_id('nowplaying')
        cards = dir_wrap.find_elements_by_class_name('list-item')
        movies = []
        for card in cards:
            item = {}
            item['name'] = card.find_element_by_css_selector('.stitle>a ').get_attribute('title')
            item['rate'] = card.find_element_by_css_selector('.subject-rate').text
            #self.dr.implicitly_wait(3)
            if item['name'] and item['rate']:
                movies.append(item)
        return sorted(movies, key=by_rate, reverse=True)

if __name__ == '__main__':
    with Douban() as douban:
        movies = douban.get_nowplaying_movies()
        print(movies)



