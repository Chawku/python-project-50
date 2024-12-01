from gendiff.formatters.selector import apply_formatter
from gendiff.parser import get_parsed_content


def make_diff(dict1: dict, dict2: dict) -> list:
    result = []
    for key in sorted(dict1.keys() | dict2.keys()):
        child1, child2 = dict1.get(key), dict2.get(key)

        if key not in dict1:
            result.append({'key': key, 'type': 'added', 'value': child2})
        elif key not in dict2:
            result.append({'key': key, 'type': 'removed', 'value': child1})
        elif isinstance(child1, dict) and isinstance(child2, dict):
            result.append({'key': key, 'type': 'nested',
                           'children': make_diff(child1, child2)})
        elif child1 != child2:
            result.append({'key': key, 'type': 'changed',
                           'old_value': child1, 'new_value': child2})
        else:
            result.append({'key': key, 'type': 'unchanged', 'value': child1})

    return result


def build_diff(dict1: dict, dict2: dict) -> dict:
    return {'type': 'root', 'children': make_diff(dict1, dict2)}


def generate_diff(file1, file2, format_of_output='stylish'):
    dict1, dict2 = get_parsed_content(file1), get_parsed_content(file2)
    diff = build_diff(dict1, dict2)
    return apply_formatter(diff, format_of_output)
