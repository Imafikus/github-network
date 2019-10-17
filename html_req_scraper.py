from requests_html import HTMLSession

import data_extractor as de
import csv_builder as cb

def get_page_from_url(url):
    
    session = HTMLSession()
    res = session.get(url)

    return res.text

def main():
    test_url = 'https://github.com/Imafikus?tab=following'
    site_data = get_page_from_url(test_url)
    
    usernames = de.extract_usernames(site_data)
    fullnames = de.extract_fullnames(site_data)

    pairs = cb.create_username_name_pairs(usernames, fullnames)
    print("Pairs: ", pairs)

if __name__ == "__main__":
    main()
    