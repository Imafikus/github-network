import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request

MAX_DEPTH = 4

class RecursiveGithubNetworkSpider(CrawlSpider):
    name = 'recursive_scraper'
    
    base_regex = '(https:\/\/github.com\/)([^\/\?]+|.+\?tab=following|.+\?tab=followers)$'
    start_urls = [
            'https://github.com/Imafikus?tab=following',
            'https://github.com/Imafikus?tab=followers',
        ]
    rules = [
            Rule(LinkExtractor(allow = base_regex), callback='parse_item', follow=True),
        
        ]

    def make_requests_from_url(self, url):
        """A method that receives a URL and returns a Request object (or a list of Request objects) to scrape. 
        This method is used to construct the initial requests in the start_requests() method, 
        and is typically used to convert urls to requests.
        """
        return Request(url, dont_filter=True, meta = {'start_url': url})

    def parse_item(self, response):
        print('CURRENT_PAGE_URL: ', response.request.meta)
        print('Parsing...')
        print(response.url)
        selected_names = Selector(response=response).css('span.f4.link-gray-dark').getall()
        selected_usernames = Selector(response=response).css('span.link-gray.pl-1').getall()
        print('SELECTED_NAMES', selected_names)
        print('SELECTED_USERNAMES', selected_usernames)

        """
            1. extract names from the start_urls
            2. create links similar to start_urls
            3. call scrape on them also
        """
    