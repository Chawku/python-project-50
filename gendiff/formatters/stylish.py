def format_diff(diff, depth=0):
    indent = '    ' * depth
    lines = []

    for item in diff['children']:
        key = item['key']
        item_type = item['type']
        value = item.get('value')
        old_value = item.get('old_value')
        new_value = item.get('new_value')

        if item_type == 'added':
            lines.append(f'{indent}  + {key}: {format_value(value, depth + 1)}')
        elif item_type == 'removed':
            lines.append(f'{indent}  - {key}: {format_value(value, depth + 1)}')
        elif item_type == 'unchanged':
            lines.append(f'{indent}    {key}: {format_value(value, depth + 1)}')
        elif item_type == 'changed':
            lines.append(f'{indent}  - {key}: {format_value(old_value, depth + 1)}')
            lines.append(f'{indent}  + {key}: {format_value(new_value, depth + 1)}')
        elif item_type == 'nested':
            nested_diff = format_diff(item, depth + 1)
            lines.append(f'{indent}    {key}: {nested_diff}')

    result = '{\n' + '\n'.join(lines) + '\n' + indent + '}'
    return result

def format_value(value, depth):
    if isinstance(value, dict):
        nested_indent = '    ' * (depth)
        lines = [f'{nested_indent}{k}: {format_value(v, depth + 1)}' for k, v in value.items()]
        return '{\n' + '\n'.join(lines) + '\n' + nested_indent + '}'
    if value is None:
        return 'null'
    return str(value).lower() if isinstance(value, bool) else str(value)

