import json
import os
import yaml


def get_parsed_content(path):
    _, extension = os.path.splitext(path)
    extension = extension.lstrip('.').lower()
    
    with open(path) as f:
        content = f.read()
    
    if extension in ('yaml', 'yml'):
        return yaml.safe_load(content)
    if extension == 'json':
        return json.loads(content)
    raise ValueError(f'Unsupported extension: {extension}')
