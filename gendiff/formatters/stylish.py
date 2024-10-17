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
            lines.append(f'{indent}  + {key}: {value}')
        elif item_type == 'removed':
            lines.append(f'{indent}  - {key}: {value}')
        elif item_type == 'unchanged':
            lines.append(f'{indent}    {key}: {value}')
        elif item_type == 'changed':
            lines.append(f'{indent}  - {key}: {old_value}')
            lines.append(f'{indent}  + {key}: {new_value}')

    result = '{\n' + '\n'.join(lines) + '\n' + indent + '}'
    return result
