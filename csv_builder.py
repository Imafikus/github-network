import os
import logging

logger = logging.getLogger(__name__)

FILE_EXT = '.csv'

def create_username_name_pairs(usernames, names):
    """
    Creates 'username (name)' format if the current name is not empty, if it is
    creates 'username'
    """
    logger.info('create username name pairs...')
    pairs = []
    for username, name in zip(usernames, names):
        
        pair = username if name == '' else username + ' (' + name + ')' 
        pairs.append(pair)
    return pairs

def format_pair(pair):
    """
    Transforms tuple (one, two) into string "one, two"
    """
    logger.info('format pair...')
    formatted_pair = pair[0] + ', ' + pair[1] + '\n'
    logger.debug('formatted_pair: ' + formatted_pair)
    return formatted_pair

def save_to_file(filename, pairs):
    """
    Saves (source, target) pairs into filename.FILE_EXT file
    """
    logger.info('save to file...')

    fname = filename + FILE_EXT
    mode = 'a' if os.path.isfile(fname) else 'w'
    logger.debug('mode is: ' + mode)

    with open(fname, mode) as f:
        for pair in pairs:
            f.write(format_pair(pair))



if __name__ == "__main__":
    pass