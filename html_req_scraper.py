from requests_html import HTMLSession

import data_extractor as de
import csv_builder as cb
import url_builder
import json_builder


MAX_RECURSION_DEPTH = 4

pairs = {}

def get_page_from_url(url):
    
    session = HTMLSession()
    res = session.get(url)

    return res.text

def create_pair(source, target):
    if source not in pairs.keys():
        pairs[source] = target

def scrape(url, current_user, recursion_depth):
    if(recursion_depth == MAX_RECURSION_DEPTH):
        return
    
    site_data = get_page_from_url(url)
    urls = []

    usernames = de.extract_usernames(site_data)
    # fullnames = de.extract_fullnames(site_data)

    for username in usernames:
        urls.append(url_builder.create_url_for_followers_tab(username))
        create_pair(username, current_user)
        # urls.append(url_builder.create_url_for_following_tab(username))

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

    json_builder.save_to_file('test.json', pairs)

if __name__ == "__main__":
    main()
    