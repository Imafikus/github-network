from requests_html import HTMLSession

import data_extractor as de
import csv_builder
import url_builder


MAX_RECURSION_DEPTH = 4

pairs = []

def get_page_from_url(url):
    
    session = HTMLSession()
    res = session.get(url)

    return res.text

def create_pair(source, target):
    """
    Creates source target pairs for saving to json
    """
    print('create_pair {} - {}'.format(source, target))
    if (source, target) not in pairs:
        pairs.append((source, target))

def is_followers_tab(url):
    if url.find('?tab=followers') != -1:
        return True 
    return False


def scrape(url, current_user, recursion_depth):
    """
    Main scraping function:

    url - target url
    current_user - current user
    recursion_depth - represents a limit for scrape
    """
    if(recursion_depth == MAX_RECURSION_DEPTH):
        return
    
    site_data = get_page_from_url(url)
    urls = []

    usernames = de.extract_usernames(site_data)

    for username in usernames:
        urls.append(url_builder.create_url_for_followers_tab(username))
        urls.append(url_builder.create_url_for_following_tab(username))
        
        if is_followers_tab(url):
            create_pair(username, current_user)
        else:
            create_pair(current_user, username)

    print('URLS')
    for url in urls:
        print(url)


def main():
    start_urls = [
        'https://github.com/Imafikus?tab=following',
        'https://github.com/Imafikus?tab=followers'
    ]

    for url in start_urls:
        scrape(url, 'Imafikus', 0)

    print('PAIRS: ', pairs)
    csv_builder.save_to_file('test', pairs)

if __name__ == "__main__":
    main()
    