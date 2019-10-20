import json
import os

def save_to_file(filename, json_dict):
    """
    Saves json_dict to filename, json_dict is in json format
    """

    exists = os.path.isfile(filename)
    if(exists):
        append_to_existing_file(filename, json_dict)
    else:
        write_into_new_file(filename, json_dict)

    
def append_to_existing_file(filename, json_dict):
    """
    if we already have existing file we want to merge json_dict with existing data
    """
    with open(filename, 'r') as f:
        data = f.read()
    
    old_dict = json.loads(data)
    for key in json_dict.keys():
        if key not in old_dict.keys():
            old_dict[key] = json_dict[key]
    
    with open(filename, 'w') as f:
        f.write(json.dumps(old_dict))


def write_into_new_file(filename, json_dict):
    """
    Writes json_dict data into a new file specified by the filenames
    """  
    with open(filename, 'w') as f:
        str_json = json.dumps(json_dict)
        f.write(str_json)