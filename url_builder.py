import logging

logger = logging.getLogger(__name__)

def create_url_for_following_tab(username):
    """
    Creates and returns the url in the following format:
    https://github.com/username?tab=following
    """
    logger.debug('create_url_for_following_tab, username = {}'.format(username))
    url = f' https://github.com/{username}?tab=following'
    return url

def create_url_for_followers_tab(username):
    """
    Creates and returns the url in the followers format:
    https://github.com/username?tab=followers
    """
    logger.debug('create_url_for_followers_tab, , username = {}'.format(username))    
    url = f' https://github.com/{username}?tab=followers'
    return url

def main():
    print(create_url_for_following_tab('Imafikus'))
    print(create_url_for_followers_tab('Imafikus'))

if __name__ == "__main__":
    main()
    
