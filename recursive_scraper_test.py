import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor

MAX_DEPTH = 4

class RecursiveGithubNetworkSpider(CrawlSpider):
    name = 'recursive_scraper'
    start_urls = [
            'https://github.com/Imafikus?tab=following',
            'https://github.com/Imafikus?tab=followers',
        ]
    rules = [
    #    Rule(LinkExtractor(allow=('(https:\/\/github.com\/)\w+(\?tab=following|\?tab=followers)',)), callback='parse', follow=True),
            # Rule(LinkExtractor(allow = r'(https:\/\/github.com\/)\w+(?!\/)'), callback='parse', follow=True),
            Rule(LinkExtractor(allow = r'(https:\/\/github.com\/)[^\/]+$'), callback='parse_item', follow=True),
        
        ]

    def parse_item(self, response):
        print('Parsing...')
        print(response.url)

        """
            1. extract names from the start_urls
            2. create links similar to start_urls
            3. call scrape on them also
        """
    