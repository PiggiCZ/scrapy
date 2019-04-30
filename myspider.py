import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.softcom.cz/eshop/foto-zrcadlovky_c12158.html?page=1&setstipagesize=1&pagesize=3000']

    def parse(self, response):
        for title in response.css('.cnt'):
            yield {'title': title.css('<h2><a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)