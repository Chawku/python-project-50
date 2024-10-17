from gendiff.formatters.stylish import format_diff as stylish
from gendiff.formatters.plain import format_diff as plain
from gendiff.formatters.json import format_diff as json


def select_formatter(diff, format_):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    if format_ in formats:
        return formats[format_](diff)

    raise ValueError(f'Unknown format: {format_}')
