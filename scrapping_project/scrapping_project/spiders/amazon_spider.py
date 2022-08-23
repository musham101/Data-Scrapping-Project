import scrapy

class amazonSpider(scrapy.Spider):
    name = 'Amazon_Spider'
    start_urls = [
        'https://www.amazon.com/s?k=top+books&crid=VP9OYY1X7W80&sprefix=top+boo%2Caps%2C345&ref=nb_sb_noss_2'
    ]
    
    def parse(self, response):
        book_name = response.css('span.a-size-base-plus.a-color-base.a-text-normal::text').extract()
        yield {'Book Names: ': book_name}