import scrapy



class BaiduSpider(scrapy.Spider):
    # 爬虫名称
    name = 'tencent'
    # 允许爬取的域名
    allowed_domains = ['www.xxx.com']
    # 爬虫基础地址 用于爬虫域名的拼接
    base_url = 'https://www.xxx.com/'
    # 爬虫入口爬取地址
    start_urls = ['https://www.xxx.com/position.php']
    # 爬虫爬取页数控制初始值
    count = 1
    # 爬虫爬取页数 10为只爬取一页
    page_end = 1

    def parse(self, response):
        pass

