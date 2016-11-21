# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import time
import re

class LagouPipeline(object):

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
    	item['companyLogo'] = 'https://www.lagou.com/' + item['companyLogo']
    	item['lastLogin'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['lastLogin']/1000.0))
    	item['positionlink'] = 'https://www.lagou.com/jobs/' + str(item['positionId']) + '.html'
    	formatCreateTime = item['formatCreateTime']
    	if '' == formatCreateTime
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
