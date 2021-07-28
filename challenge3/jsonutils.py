import json
from jsonpath_ng import jsonpath, parse

def get_value_from_json(data, key):
    json_data = json.loads(data)

    key_list = key.split('/')
    path = ''
    for key in key_list:
        path+= '['+key+']'
    
    jsonpath_expression = parse('$'+path)
    match = jsonpath_expression.find(json_data)

    return match[0].value