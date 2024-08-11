import scrapy


class SvetsSpider(scrapy.Spider):
    name = "svets"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svetsvet = response.css('div.i4dRQ')
        for svety in svetsvet:
            yield {
                'name': svety.css('div.lsooF span::text').get(),
                'price': svety.css('div.pY3d2 span::text').get(),
                'url': svety.css('a').attrib['href']
            }
