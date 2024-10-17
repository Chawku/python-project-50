import json
import os
import yaml


def get_file_format(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lstrip('.').lower()


def get_file_content(file_name):
    with open(file_name) as f:
        return f.read()


def parse_content(content, extension):
    if extension in ('yaml', 'yml'):
        return yaml.safe_load(content)
    if extension == 'json':
        return json.loads(content)
    raise ValueError(f'Unsupported extension: {extension}')


def parse_file(file_name):
    content = get_file_content(file_name)
    extension = get_file_format(file_name)
    return parse_content(content, extension)
