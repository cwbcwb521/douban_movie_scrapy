# -*- coding: utf-8 -*-
import scrapy
from douban_movie.items import DoubanMovieItem
import re
from scrapy.http import Request
import time
import random

START = 0

class MovieSpiderSpider(scrapy.Spider):
    name = "movie_spider"
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=电影&start=0',
    )

    def parse(self, response):
        time.sleep(random.randint(2, 5))
        global START
        item = DoubanMovieItem()
        # https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20
        # while True:
        pat_title = r'title":"(.*?)"'
        pat_rate = r'rate":"(.*?)"'
        pat_url = r'url":"(.*?)"'
        item['title'] = re.compile(pat_title).findall(str(response.body.decode('utf-8')))
        item['rate'] = re.compile(pat_rate).findall(str(response.body.decode('utf-8')))
        item['url'] = re.compile(pat_url).findall(str(response.body.decode('utf-8')))
        print(item['title'])
        if item['title'] == []:
            exit()
        print('return item success')
        yield item
        print('yield item success')

        next_url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E7%94%B5%E5%BD%B1&start='
        START = START + 20
        print('next url :' + next_url+str(START) )
        yield Request(next_url+str(START),callback=self.parse,headers={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"},encoding='utf-8')
        print('yield request success')
