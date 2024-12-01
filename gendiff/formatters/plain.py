def format_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, (int, float)):
        return str(value)
    return '[complex value]'


def walk(node, path):
    lines = []
    for child in node['children']:
        property_path = (
            f"{path}.{child['key']}" if path else child['key']
        )
        if child['type'] == 'added':
            value = format_value(child['value'])
            lines.append(
                f"Property '{property_path}' was added with value: {value}"
            )
        elif child['type'] == 'removed':
            lines.append(
                f"Property '{property_path}' was removed"
            )
        elif child['type'] == 'changed':
            old_value = format_value(child['old_value'])
            new_value = format_value(child['new_value'])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif child['type'] == 'nested':
            lines.append(walk(child, property_path))
    return '\n'.join(lines)


def format_diff(diff):
    return walk(diff, "")
