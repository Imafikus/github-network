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

if __name__ == "__main__":
    pass