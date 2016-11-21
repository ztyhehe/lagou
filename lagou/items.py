# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field


class LagouItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companySize = Field()
    firstType = Field()
    appShow = Field()
    pcShow = Field()
    positionName = Field()
    education = Field()
    financeStage = Field()
    city = Field()
    companyLogo = Field()
    district = Field()
    companyId = Field()
    explain = Field()
    industryField = Field()
    createTime = Field()
    positionLables = Field()
    score = Field()
    adWord = Field()
    formatCreateTime = Field()
    salary = Field()
    workYear = Field()
    lastLogin = Field()
    jobNature = Field()
    deliver = Field()
    gradeDescription = Field()
    imState = Field()
    companyFullName = Field()
    companyLabelList = Field()
    positionId = Field()
    companyShortName = Field()
    approve = Field()
    businessZones = Field()
    plus = Field()
    secondType = Field()
    positionAdvantage = Field()
    publisherId = Field()
    promotionScoreExplain = Field()
    positionlink = Field()