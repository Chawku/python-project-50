import pytest
from gendiff.formatters.plain import format_diff


def test_format_diff_plain():
    diff = {
        'type': 'root',
        'children': [
            {'key': 'common.follow', 'type': 'added', 'value': False},
            {'key': 'common.setting2', 'type': 'removed'},
            {'key': 'common.setting3', 'type': 'changed', 'old_value': True, 'new_value': None},
            {'key': 'common.setting4', 'type': 'added', 'value': 'blah blah'},
            {'key': 'common.setting5', 'type': 'added', 'value': [1, 2, 3]},
            {'key': 'common.setting6.doge.wow', 'type': 'changed', 'old_value': '', 'new_value': 'so much'},
            {'key': 'common.setting6.ops', 'type': 'added', 'value': 'vops'},
            {'key': 'group1.baz', 'type': 'changed', 'old_value': 'bas', 'new_value': 'bars'},
            {'key': 'group1.nest', 'type': 'changed', 'old_value': [1, 2], 'new_value': 'str'},
            {'key': 'group2', 'type': 'removed'},
            {'key': 'group3', 'type': 'added', 'value': [1, 2, 3]},
        ]
    }

    expected_output = (
        "Property 'common.follow' was added with value: False\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From True to None\n"
        "Property 'common.setting4' was added with value: blah blah\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From  to so much\n"
        "Property 'common.setting6.ops' was added with value: vops\n"
        "Property 'group1.baz' was updated. From bas to bars\n"
        "Property 'group1.nest' was updated. From [complex value] to str\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )

    assert format_diff(diff) == expected_output
