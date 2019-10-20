import json

def save_to_file(filename, json_dict):
    with open(filename, 'w') as f:
        str_json = json.dumps(json_dict)
        f.write(str_json)