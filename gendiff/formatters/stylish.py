def format_value(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        return '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def stylish(diff, depth=0):
    indent = '    ' * depth
    result = []

    for node in diff['children']:
        key = node['key']
        if node['type'] == 'added':
            result.append(f"{indent}  + {key}: {format_value(node['value'], depth + 1)}")
        elif node['type'] == 'removed':
            result.append(f"{indent}  - {key}: {format_value(node['value'], depth + 1)}")
        elif node['type'] == 'changed':
            result.append(f"{indent}  - {key}: {format_value(node['old_value'], depth + 1)}")
            result.append(f"{indent}  + {key}: {format_value(node['new_value'], depth + 1)}")
        elif node['type'] == 'unchanged':
            result.append(f"{indent}    {key}: {format_value(node['value'], depth + 1)}")
        elif node['type'] == 'nested':
            result.append(f"{indent}    {key}: {{")
            result.append(stylish(node, depth + 1))
            result.append(f"{indent}    }}")

    if depth == 0:
        return '{\n' + '\n'.join(result) + '\n}'
    return '\n'.join(result)


def format_diff(diff):
    return stylish(diff)
