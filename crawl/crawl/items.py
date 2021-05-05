# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #分类
    yclass = scrapy.Field()
    #页数
    ypage = scrapy.Field()
    #视频名称
    yname = scrapy.Field()
    #下载地址
    yurl = scrapy.Field()
    pass
