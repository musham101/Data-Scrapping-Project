import scrapy

class amazonSpider(scrapy.Spider):
    name = 'Reddit_Spider'
    start_urls = [
        'https://www.reddit.com/r/sports/'
    ]
    
    def parse(self, response):
        post_title = response.css('h3._eYtD2XCVieq6emjKBH3m::text').extract()
        time = response.css('span._2VF2J19pUIMSLJFky-7PEI::text').extract()
        up_votes = response.css('div._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo::text').extract()
        yield {'Post Title: ': post_title, 'Time:' : time, 'Likes:' : up_votes}