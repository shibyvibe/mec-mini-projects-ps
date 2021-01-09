import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_xpath"

#    start_urls = ["http://quotes.toscrape.com/page/1/"] #, "http://quotes.toscrape.com/page/2/"]  ** INTERESTING - if page 2 is included it is parsed twice in this case !!!!
    def start_requests(self):
            urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       self.log(">>>> Response URL: " + response.url)

       for quote in response.xpath("//div[@class='quote']"):
            yield {
               'source': response.url,
               'text': quote.xpath("span[@class='text']/text()").get(),
               'author': quote.xpath("span/small[@class='author']/text()").get(),
               'tags': quote.xpath("div[@class='tags']/a[@class='tag']/text()").getall(),
            }
 
       next_page = response.xpath("//li[@class='next']/a/@href").get()
       if next_page is not None:
           next_page = response.urljoin(next_page)
           yield response.follow(next_page, callback=self.parse)

#       yield response.follow_all(response.xpath("//li[@class='next']/a"), callback=self.parse);
