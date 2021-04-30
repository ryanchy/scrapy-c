import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['demo']
    start_urls = ['http://demo/']

    def parse(self, response):
        pass
