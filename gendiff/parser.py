import json
import os

import yaml


def parse(content, format):
    format = format.lower()
    if format in ('yaml', 'yml'):
        return yaml.safe_load(content)
    if format == 'json':
        return json.loads(content)
    raise ValueError(f"Unsupported format: {format}")


def get_parsed_content(path):
    _, extension = os.path.splitext(path)
    extension = extension.lstrip('.').lower()

    with open(path) as f:
        content = f.read()

    return parse(content, extension)
