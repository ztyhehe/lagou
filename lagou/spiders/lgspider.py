# coding:utf-8

import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.selector import Selector
import json

from lagou.items import LagouItem

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/jobs/positionAjax.json?']

    urls = 'https://www.lagou.com/jobs/positionAjax.json?'

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Host": "www.lagou.com",
        "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36",
        "Referer": "https://www.lagou.com/jobs/list_Python?"
    }

    # def make_requests_from_url(self, url):
    #     return Request(url, dont_filter=True, method='POST', meta={'first':'false','pn':'2','kd':'Python'})

    # def after_post(self, response):
    #     print response.body
    pn = 1

    def start_requests(self, pn=1):
        for url in self.start_urls:
            # first = 'true' if 1==pn else 'false'
            # print first
            # print pn
            # formdata={'first':''+first+'','pn':''+str(pn)+'','kd':'Python'}
            # print formdata
            # self.parse()
            # print '11111111111111111111111111111' 'kd':'Python'
            yield FormRequest(url=url, headers=self.headers, formdata={'first':'false', 'pn':'1',}, callback=self.parse)

    # def for_result(self, result):
    #     print '------------------------------'
    #     for i in result:
    #         # print i
    #         item['companySize'] = i['companySize']
    #         # print companySize
    #         # print i['companySize']
    #         item['firstType'] = i['firstType']
    #         item['appShow'] = i['appShow']
    #         item['pcShow'] = i['pcShow']
    #         item['positionName'] = i['positionName']
    #         item['education'] = i['education']
    #         item['financeStage'] = i['financeStage']
    #         item['city'] = i['city']
    #         item['companyLogo'] = i['companyLogo']
    #         item['district'] = i['district']
    #         item['companyId'] = i['companyId']
    #         item['explain'] = i['explain']
    #         item['industryField'] = i['industryField']
    #         item['createTime'] = i['createTime']
    #         item['positionLables'] = i['positionLables']
    #         item['score'] = i['score']
    #         item['adWord'] = i['adWord']
    #         item['formatCreateTime'] = i['formatCreateTime']
    #         item['salary'] = i['salary']
    #         item['workYear'] = i['workYear']
    #         item['lastLogin'] = i['lastLogin']
    #         item['jobNature'] = i['jobNature']
    #         item['deliver'] = i['deliver']
    #         item['gradeDescription'] = i['gradeDescription']
    #         item['imState'] = i['imState']
    #         item['companyFullName'] = i['companyFullName']
    #         item['companyLabelList'] = i['companyLabelList']
    #         item['positionId'] = i['positionId']
    #         item['companyShortName'] = i['companyShortName']
    #         item['approve'] = i['approve']
    #         item['businessZones'] = i['businessZones']
    #         item['plus'] = i['plus']
    #         item['secondType'] = i['secondType']
    #         item['positionAdvantage'] = i['positionAdvantage']
    #         item['publisherId'] = i['publisherId']
    #         item['promotionScoreExplain'] = i['promotionScoreExplain']
    #         yield item

    def parse(self, response):
        # print response.body

        # print '**************************************'
        # return [FormRequest(url=self.urls, formdata={'first':'false','pn':'2','kd':'Python'}, callback=self.after_post)]

        # # print aa.encode('utf-8')
        # # print aa
        # try:
        #     print type(aa)
        #     # print aa.response.body
        # except:
        #     print 'chucuo'
        # print '-----------------------------------------'

        # return [FormRequest(url="http://www.example.com/post/action", formdata={'name': 'John Doe', 'age': '27'}, callback=self.after_post)]
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)



        item = LagouItem()
        # items = []
        infojson = json.loads(response.body)
        result=infojson['content']['positionResult']['result']
        if result:
            # print result
            # self.for_result(result)
            for i in result:
                # print i
                item['companySize'] = i['companySize']
                # print companySize
                # print i['companySize']
                item['firstType'] = i['firstType']
                item['appShow'] = i['appShow']
                item['pcShow'] = i['pcShow']
                item['positionName'] = i['positionName']
                item['education'] = i['education']
                item['financeStage'] = i['financeStage']
                item['city'] = i['city']
                item['companyLogo'] = i['companyLogo']
                item['district'] = i['district']
                item['companyId'] = i['companyId']
                item['explain'] = i['explain']
                item['industryField'] = i['industryField']
                item['createTime'] = i['createTime']
                item['positionLables'] = i['positionLables']
                item['score'] = i['score']
                item['adWord'] = i['adWord']
                item['formatCreateTime'] = i['formatCreateTime']
                item['salary'] = i['salary']
                item['workYear'] = i['workYear']
                item['lastLogin'] = i['lastLogin']
                item['jobNature'] = i['jobNature']
                item['deliver'] = i['deliver']
                item['gradeDescription'] = i['gradeDescription']
                item['imState'] = i['imState']
                item['companyFullName'] = i['companyFullName']
                item['companyLabelList'] = i['companyLabelList']
                item['positionId'] = i['positionId']
                item['companyShortName'] = i['companyShortName']
                item['approve'] = i['approve']
                item['businessZones'] = i['businessZones']
                item['plus'] = i['plus']
                item['secondType'] = i['secondType']
                item['positionAdvantage'] = i['positionAdvantage']
                item['publisherId'] = i['publisherId']
                item['promotionScoreExplain'] = i['promotionScoreExplain']
                yield item

            self.pn += 1
            while 1:
                first = 'true' if 1==self.pn else 'false'
                # print first
                # print pn
                # formdata={'first':''+first+'','pn':''+str(pn)+'','kd':'Python'}
                # print formdata
                # self.parse()
                # print '1222222222222222222222222222222''kd':'Python'
                yield FormRequest(url=self.urls, headers=self.headers, formdata={'first':first, 'pn':str(self.pn), }, callback=self.parse)
        else:
            print '-----------------------------------------------'
            print 'haoxiangmeiyoule'
            print '-----------------------------------------------'
            return
            # items.append(item)
        # items.append(item)
        # return item
