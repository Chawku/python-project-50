import os
import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture
def json_file1():
    return os.path.join("tests/fixtures", "file1.json")


@pytest.fixture
def json_file2():
    return os.path.join("tests/fixtures", "file2.json")


def test_generate_diff_json(json_file1, json_file2):
    expected_json_output = """{
  "type": "root",
  "children": [
    {
      "key": "follow",
      "type": "removed",
      "value": false
    },
    {
      "key": "host",
      "type": "unchanged",
      "value": "hexlet.io"
    },
    {
      "key": "proxy",
      "type": "removed",
      "value": "123.234.53.22"
    },
    {
      "key": "timeout",
      "type": "changed",
      "old_value": 50,
      "new_value": 20
    },
    {
      "key": "verbose",
      "type": "added",
      "value": true
    }
  ]
}"""

    assert generate_diff(json_file1, json_file2, format_of_output='json') == expected_json_output
