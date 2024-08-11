

import scrapy
import csv

class SvetsSpider(scrapy.Spider):
    name = "svets"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svetsvet = response.css('div.i4dRQ')
        parsed_data = []

        for svety in svetsvet:
            item = {
                'name': svety.css('div.lsooF span::text').get(),
                'price': svety.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(svety.css('a').attrib['href'])  # Полный URL
            }
            parsed_data.append(item)

        # Сохраняем данные в CSV
        self.save_to_csv(parsed_data)

    def save_to_csv(self, data):
        with open("svets_data.csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'price', 'url'])
            writer.writeheader()
            writer.writerows(data)