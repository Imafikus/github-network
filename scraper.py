import scrapy
from scrapy.selector import Selector

class GithubNetworkSpider(scrapy.Spider):
    name = 'github_scraper'
    HTTP_PART = 6
    HTTPS_PART = 7
    HTML_EXT = '.html'
    
    def start_requests(self):
        urls = ['https://github.com/Imafikus?tab=following']

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        #self.save_html_to_file(response)
        self.extract_data_based_on_tags(response)

    
    def extract_data_based_on_tags(self, response):
        selected_data = Selector(response=response).css('span.f4.link-gray-dark').getall()
        for data in selected_data:
            print("SELECTED_DATA: ", data)

    def save_html_to_file(self, response):
        """
        Saves .html data got from the response
        """
        fname = self.create_file_name_from_url(response.url)
        print('FNAME: ', fname)
        with open(fname, 'w') as f:
            f.write(response.body.decode('utf-8'))
        self.log('save_html_to_file...')
    
    def create_file_name_from_url(self, url):
        """
        Receive url and create proper .html file from it
        """
        if(url.find('https')):
            fname = url[self.HTTPS_PART:]
        else:
            fname = url[self.HTTP_PART:]
        fname = fname.replace('/', '-')
        fname += self.HTML_EXT
        return fname
        