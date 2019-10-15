import scrapy
from scrapy.selector import Selector
import html_parser as hp

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
        print('CURRENT_PAGE_URL: ', response.request.url)
        self.extract_current_user(response)
        self.extract_data_based_on_tags(response)

    
    def extract_data_based_on_tags(self, response):

        selected_names = Selector(response=response).css('span.f4.link-gray-dark').getall()
        selected_usernames = Selector(response=response).css('span.link-gray.pl-1').getall()
        
        extracted_names = []
        for data in selected_names:
            extracted_names.append(self.extract_data_from_html(data))
        
        extracted_usernames = []
        for data in selected_usernames:
            extracted_usernames.append(self.extract_data_from_html(data))
        
        combined_data = self.combine_name_and_username(extracted_names, extracted_usernames)
        print("COMBINED: ", combined_data)
        return combined_data

    def combine_name_and_username(self, names, usernames):
        combined_data = []

        for i in range(0, len(names)):
            name = names[i]
            username = usernames[i]
            
            if(name == ''):
                combined_data.append(username)
            else:
                combined_data.append(username +' (' + name + ')')
        return combined_data

    def extract_data_from_html(self, html_string):
        """
        Extract only name/ username from span tags received as html_string
        """
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
    
    def save_csv_data(self, response):
        print("RESPONSE_URL", response.url)
        combined_data = self.extract_data_based_on_tags(response)
        if self.is_following_url(response.url):
            self.create_csv_data(combined_data, True)
        else:
            self.create_csv_data(combined_data, following=False)
        
    
    def is_following_url(self, url):
        return True if url.find('?tab=following') != -1 else False
    
    def create_csv_data(self, combined_data, following):
        print('create_csv_data, following = ', following)

    def extract_current_user(self, response):
        selected_html_name = Selector(response=response).css('span.p-name.vcard-fullname.d-block.overflow-hidden').get()
        selected_html_username = Selector(response=response).css('span.p-nickname.vcard-username.d-block').get()
        

        extracted_name = self.extract_data_from_html(selected_html_name)
        extracted_username = self.extract_data_from_html(selected_html_username)

        if extracted_name != " ":
            current_user = extracted_username + " (" + extracted_name + ")"
        else:
            current_user = extracted_username
        print("CURRENT_USER: ", current_user)
        return current_user