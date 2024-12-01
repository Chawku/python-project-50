def format_value(value, depth):
    indent = '    ' * depth
    if isinstance(value, dict):
        lines = [
            f"{indent}    {k}: {format_value(v, depth + 1)}"
            for k, v in value.items()
        ]
        return '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def format_added(node, depth, indent):
    value = format_value(node['value'], depth + 1)
    return f"{indent}  + {node['key']}: {value}"


def format_removed(node, depth, indent):
    value = format_value(node['value'], depth + 1)
    return f"{indent}  - {node['key']}: {value}"


def format_changed(node, depth, indent):
    old_value = format_value(node['old_value'], depth + 1)
    new_value = format_value(node['new_value'], depth + 1)
    return (
        f"{indent}  - {node['key']}: {old_value}\n"
        f"{indent}  + {node['key']}: {new_value}"
    )


def format_unchanged(node, depth, indent):
    value = format_value(node['value'], depth + 1)
    return f"{indent}    {node['key']}: {value}"


def format_nested(node, depth, indent):
    nested_header = f"{indent}    {node['key']}: {{"
    nested_content = stylish(node, depth + 1)
    nested_footer = f"{indent}    }}"
    return f"{nested_header}\n{nested_content}\n{nested_footer}"


def stylish(diff, depth=0):
    indent = '    ' * depth
    result = []

    handlers = {
        'added': format_added,
        'removed': format_removed,
        'changed': format_changed,
        'unchanged': format_unchanged,
        'nested': format_nested,
    }

    for node in diff['children']:
        node_type = node['type']
        handler = handlers[node_type]
        result.append(handler(node, depth, indent))

    if depth == 0:
        return '{\n' + '\n'.join(result) + '\n}'
    return '\n'.join(result)


def format_diff(diff):
    return stylish(diff)
