'''获取豆瓣正在热映电影和读书中的内容'''
from selenium import webdriver
import time

class Douban(object):

    def __init__(self):
        self.book_url = 'https://book.douban.com'
        self.movie_url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
        self.dr = webdriver.Chrome()

    def __enter__(self):
        pass

    def __exit__(self):
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
            item['rate'] = card.find_element_by_css_selector('.srating').text
            if item['name'] and item['rate']:
                movies.append(item)
            return sorted(movies, key=by_rate, reverse=True)

if __name__ == '__main__':
    douban = Douban()
    douban.get_nowplaying_movies()



