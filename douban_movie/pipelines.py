# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import json


class DoubanMoviePipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['电影名称', '评分', '网址'])

    def process_item(self, item, spider):
        # url = item['url'][0].replace('\\', '')
        # self.ws.append([item['title'][0],item['rate'][0], url])
        # self.wb.save('/Users/slothgreed/scrapy_study/scrapy_workplace/douban_movie/movie.xlsx')

        for i in range (len(item['title'])):
            url = item['url'][i].replace('\\', '')
            line = [item['title'][i], item['rate'][i], url]
            self.ws.append(line)
            self.wb.save('/Users/slothgreed/scrapy_study/scrapy_workplace/douban_movie/movie.xlsx')

        return item
