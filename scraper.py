import scrapy
from scrapy.selector import Selector

class GithubNetworkSpider(scrapy.Spider):
    name = 'github_scraper'
    HTTP_PART = 6
    HTTPS_PART = 7
    HTML_EXT = '.html'
    
    def start_requests(self):
        urls = [
            'https://github.com/Imafikus?tab=following',
            'https://github.com/Imafikus?tab=followers',
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        #self.save_html_to_file(response)
        self.extract_data_based_on_tags(response)

    
    def extract_data_based_on_tags(self, response):
        selected_names = Selector(response=response).css('span.f4.link-gray-dark').getall()
        selected_usernames = Selector(response=response).css('span.link-gray.pl-1').getall()
        for data in selected_names:
            print("SELECTED_NAMES: ", self.extract_names_from_html(data))
        print("LEN(SELECTED_NAMES)", len(selected_names))

        for data in selected_usernames:
            print("SELECTED_USERNAMES: ", self.extract_names_from_html(data))
        print("LEN(SELECTED_USERNAMES)", len(selected_usernames))


        print("EQUAL: ",len(selected_names) == len(selected_usernames))
    def extract_names_from_html(self, html_string):
        begin = '">'
        end = "</" 

        s = html_string.find(begin) + len(begin)
        e = html_string.find(end)
        return html_string[s:e]

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
        