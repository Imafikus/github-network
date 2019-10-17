

def create_username_name_pairs(usernames, names):
    """
    Creates 'username (name)' format if the current name is not empty, if it is
    creates 'username'
    """
    pairs = []
    for username, name in zip(usernames, names):
        
        pair = username if name == '' else username + ' (' + name + ')' 
        pairs.append(pair)
    return pairs
if __name__ == "__main__":
    pass