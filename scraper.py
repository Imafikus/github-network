import scrapy

class GithubNetworkSpider(scrapy.Spider):
    name = 'github_scraper'
    
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/']

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        with open('test.html', 'w') as test:
            test.write(response.body.decode('utf-8'))
        self.log('Saved file...')