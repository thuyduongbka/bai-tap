import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com'        
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):     
        data = []   
        for quote in response.css('div.quote'):
            res = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }    
            data.append(res)
        print("DATA: \n",data)
