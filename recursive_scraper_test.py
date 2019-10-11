import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

MAX_DEPTH = 4

class RecursiveGithubNetworkSpider(CrawlSpider):
    name = 'recursive_scraper'
    start_urls = [
            'https://github.com/Imafikus?tab=following',
            'https://github.com/Imafikus?tab=followers',
        ]
    rules = [
        Rule(LinkExtractor(allow=('(https:\/\/github.com\/)\w+(\?tab=following|\?tab=followers)',)), callback='parse', follow=True),
        ]

    def parse(self, response):
        print('Parsing...')
        print(response.url)

    