import pytest
import os
from gendiff import generate_diff


@pytest.fixture
def file1_tree():
    return os.path.join("tests/fixtures", "file1_tree.yaml")


@pytest.fixture
def file2_tree():
    return os.path.join("tests/fixtures", "file2_tree.yaml")


def test_format_diff(file1_tree, file2_tree):
    expected_output = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    diff = generate_diff(file1_tree, file2_tree, format_of_output='stylish')
    assert ''.join(diff.split()) == ''.join(expected_output.split())
