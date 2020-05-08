import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    data = []

    def start_requests(self):
        url = 'http://quotes.toscrape.com'        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):             
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }                
            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)    
