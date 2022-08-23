import scrapy


class amazonSpider(scrapy.Spider):
    name = 'Test_Spider'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]
    
    def parse(self, response):

        qoute = response.css('span.text::text').extract()
        author = response.css('small.author::text').extract()

        yield {
            'Qoutes' : qoute,
            'Author' : author
        }
        