import pytest
from gendiff.generate_diff import make_diff, build_diff, generate_diff
import json
import os


@pytest.fixture
def dict1():
    with open(os.path.join("tests/fixtures", "file1.json")) as f:
        return json.load(f)


@pytest.fixture
def dict2():
    with open(os.path.join("tests/fixtures", "file2.json")) as f:
        return json.load(f)


def test_make_diff(dict1, dict2):
    expected = [
        {'key': 'follow', 'type': 'removed', 'value': False},
        {'key': 'host', 'type': 'unchanged', 'value': 'hexlet.io'},
        {'key': 'proxy', 'type': 'removed', 'value': '123.234.53.22'},
        {'key': 'timeout', 'type': 'changed', 'old_value': 50, 'new_value': 20},
        {'key': 'verbose', 'type': 'added', 'value': True},
    ]
    assert make_diff(dict1, dict2) == expected


def test_build_diff(dict1, dict2):
    expected = {
        'type': 'root',
        'children': [
            {'key': 'follow', 'type': 'removed', 'value': False},
            {'key': 'host', 'type': 'unchanged', 'value': 'hexlet.io'},
            {'key': 'proxy', 'type': 'removed', 'value': '123.234.53.22'},
            {'key': 'timeout', 'type': 'changed', 'old_value': 50, 'new_value': 20},
            {'key': 'verbose', 'type': 'added', 'value': True},
        ]
    }
    assert build_diff(dict1, dict2) == expected


def test_generate_diff():
    file1 = os.path.join("tests/fixtures", "file1.json")
    file2 = os.path.join("tests/fixtures", "file2.json")

    expected_stylish_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    assert generate_diff(file1, file2, format_of_output='stylish') == expected_stylish_output
