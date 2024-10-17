def format_diff(diff):
    def format_line(key, change_type, value1=None, value2=None):
        if change_type == 'added':
            return f"Property '{key}' was added with value: {format_value(value2)}"
        elif change_type == 'removed':
            return f"Property '{key}' was removed"
        elif change_type == 'changed':
            return f"Property '{key}' was updated. From {format_value(value1)} to {format_value(value2)}"
        return ''

    def format_value(value):
        if isinstance(value, dict) or isinstance(value, list):
            return '[complex value]'
        return value if value is not None else 'None'

    def format_nested(parent_key, children):
        result = []
        for item in children:
            key = f"{parent_key}.{item['key']}"
            change_type = item['type']
            if change_type == 'added':
                result.append(format_line(key, change_type, value2=item.get('value')))
            elif change_type == 'removed':
                result.append(format_line(key, change_type))
            elif change_type == 'changed':
                result.append(format_line(key, change_type, value1=item.get('old_value'), value2=item.get('new_value')))
            elif change_type == 'nested':
                result.extend(format_nested(key, item['children']))
        return result

    result = []
    for item in diff['children']:
        key = item['key']
        change_type = item['type']
        if change_type in ['added', 'removed']:
            result.append(format_line(key, change_type, value2=item.get('value')))
        elif change_type == 'changed':
            result.append(format_line(key, change_type, value1=item.get('old_value'), value2=item.get('new_value')))
        elif change_type == 'nested':
            result.extend(format_nested(key, item['children']))

    return '\n'.join(result)
