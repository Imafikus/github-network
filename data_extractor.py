import re
import logging

logger = logging.getLogger(__name__)

def extract_usernames(html):
    """
    Extracts usernames from span tag in html. Tags are in the following format:
    <span class="link-gray pl-1">some_username</span>
    """
    logger.debug('extract_usernames...')
    regex = re.compile(r'\s*<span class="link-gray pl-1">(?P<username>.*)</span>')
    usernames = []

    for m in regex.finditer(html):
        usernames.append(m.group('username'))

    return usernames

def extract_fullnames(html):
    """
    Extracts fullnames from span tag in html. Tags are in the following format:
    <span class="link-gray pl-1">some_username</span>
    """
    logger.debug('extract_fullnames...')

    regex = re.compile(r'\s*<span class="f4 link-gray-dark">(?P<fullname>.*)</span>')
    fullnames = []

    for m in regex.finditer(html):
        fullnames.append(m.group('fullname'))

    return fullnames

def extract_username_from_url(url):
    """
    Extract username from the following / followers url
    """
    logger.debug('extracting username from: {}'.format(url))
    regex = re.compile(r'https://github.com/(?P<username>.*)\?tab=(following|followers)')
    m = regex.search(url)
    logger.debug('match = {}'.format(m))
    username = m.group('username')
    return username



if __name__ == "__main__":
    print(type(('https://github.com/birantaltinel?tab=following')))
    print(type(('https://github.com/birantaltinel?tab=followers')))