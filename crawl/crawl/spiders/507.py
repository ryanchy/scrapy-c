import scrapy, random
from crawl.items import YgItem
import re

class YgSpider(scrapy.Spider):
    USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    name = 'yg'
    allowed_domains = ['www.032pa.com']
    start_urls = ['https://www.032pa.com/']
    header_str = """:authority: www.016pa.com
                :method: GET
                :path: /
                :scheme: https
                accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
                accept-encoding: gzip, deflate, br
                accept-language: zh-CN,zh;q=0.9
                cache-control: max-age=0
                cookie: guid=781e142d56932d9f31eda65f17fa8201; HstCfa4166711=1620233401695; HstCla4166711=1620233401695; HstCmu4166711=1620233401695; HstPn4166711=1; HstPt4166711=1; HstCnv4166711=1; HstCns4166711=1; c_ref_4166711=https%3A%2F%2Fwww.002pa.com%2F; __dtsu=104016197206910740FB9B6CE6EAFC5A
                if-modified-since: Wed, 05 May 2021 16:10:05 GMT
                if-none-match: W/"6092c35d-6298"
                sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
                sec-ch-ua-mobile: ?0
                sec-fetch-dest: document
                sec-fetch-mode: navigate
                sec-fetch-site: cross-site
                sec-fetch-user: ?1
                upgrade-insecure-requests: 1
                user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"""
    headers = dict([line.strip().split(": ", 1) for line in header_str.split("\n")])
    headers["user-agent"] = random.choice(USER_AGENT_LIST)
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)
        print("ok")
    def parse(self, response):

        item = YgItem()
        class_list = response.xpath("//ul/li/a/text()").extract()
        class_url_list = response.xpath("//li/a").css("a::attr(href)").extract()
        # print(class_list)
        # print(class_url_list)
        # print(len(class_url_list))
        i = 0
        for i in (3,2):
            item["yclass"] = class_list[i]

            print(class_url_list[i])
            yield scrapy.Request(url="https://www.032pa.com{}".format(class_url_list[i]), meta={"item":item}, callback=self.class_parse)
    def class_parse(self, response):
        item = response.meta["item"]
        print(item)pageend = response.xpath("//ul/font/a").extract()[-1]
        print(pageend)
        abc =re.compile(r".*index-(\d*)", re.S)
        ab = abc.findall(pageend)
        # for j in range(1, int(ab[0])):
        for j in range(1, 4):

            item["ypage"] = j
            print(item)
            print(response.url+"index-{}.html".format(j))
            yield scrapy.Request(url=response.url+"index-{}.html".format(j), meta={"item":item}, callback=self.page_parse)
    #
    #
    def page_parse(self, response):
        item = response.meta["item"]
        print(item)
        # videos = response.xpath("//section/div/div/div/div/div/a").css("[target]").extract()
        # # for e in videos:
        # # print(videos.xpath("//div/div/a").css("[target='_blank']").css("[href]").extract())
        # videos_list = []
        # for x in videos:
        #     videos_list.append(re.findall(r"(Html.*?html)", x, re.M)[0])
        # print(videos_list,item["ypage"])
            # print(videos_urls)
        # for v in videos:
        #     video_url = v.xpass("//a").extract_first()
        #     print(video_url)