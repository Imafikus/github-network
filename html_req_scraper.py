from requests_html import HTMLSession

import data_extractor
import csv_builder
import url_builder
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


MAX_RECURSION_DEPTH = 1

pairs = []

# if we don't mark them, we will have duplicated data for the Imafikus
already_visited_urls = [
    'https://github.com/Imafikus?tab=following',
    'https://github.com/Imafikus?tab=followers'
]

def get_page_from_url(url):
    
    session = HTMLSession()
    res = session.get(url)

    return res.text

def create_pair(source, target):
    """
    Creates source-target pairs for saving to csv, works with global pairs variable
    """
    logger.debug('create_pair {} - {}'.format(source, target))
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
    logger.debug('scrape with recursion_depth = {}, current_user = {}'.format(recursion_depth, current_user))
    if recursion_depth > MAX_RECURSION_DEPTH:
        logger.debug('Maximum recursion depth reached, exiting...')
        return
    
    site_data = get_page_from_url(url)
    urls = []

    usernames = data_extractor.extract_usernames(site_data)

    for username in usernames:
        urls.append(url_builder.create_url_for_followers_tab(username))
        urls.append(url_builder.create_url_for_following_tab(username))
        
        if is_followers_tab(url):
            create_pair(username, current_user)
        else:
            create_pair(current_user, username)
        
    for url in urls:
        if url not in already_visited_urls:
            already_visited_urls.append(url)
            next_user = data_extractor.extract_username_from_url(url)
            scrape(url, next_user, recursion_depth + 1)

def main():
    start_urls = [
        'https://github.com/Imafikus?tab=following',
        'https://github.com/Imafikus?tab=followers'
    ]

    for url in start_urls:
        scrape(url, 'Imafikus', 0)

    csv_builder.save_to_file('test', pairs)

if __name__ == "__main__":
    main()
    