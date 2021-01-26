import scrapy


class A74ruSpider(scrapy.Spider):
    name = '74ru'
    allowed_domains = ['74.ru']
    start_urls = ['https://74.ru/']

    custom_settings = {'FEED_URI': "74ru.csv", 'FEED_FORMAT': 'csv'}

    def parse(self, response):
        print("procesing: " + response.url)

        # LHcp - Воскресенье
        # LJef - Понедельник
        # LRed - Вторник
        urls = response.xpath("//div[@class='LRed']/div/article/a/@href").extract()
        # print(urls)
        count = 0
        for url in urls:
            if 'longread' in url:
                continue
            yield scrapy.Request(response.urljoin(url), callback=self.get_text)
            count += 1
            if count > 5:
                break

    def get_text(self, response):
        title = response.xpath("//div[@class='F1act']/h2/span/text()").extract_first()
        text = response.xpath("//div[@class='BPh9']/div/div/div/div/p/text()").extract()
        full_text = ' '.join(text)

        yield {'url': response.url,
               'title': title,
               'text': full_text}

