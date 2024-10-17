import os
import pytest
from gendiff.generate_diff import generate_diff


@pytest.fixture
def yaml_file1():
    return os.path.join("tests/fixtures", "file1.yaml")


@pytest.fixture
def yaml_file2():
    return os.path.join("tests/fixtures", "file2.yaml")


def test_generate_diff_yaml(yaml_file1, yaml_file2):
    expected_stylish_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    assert generate_diff(yaml_file1, yaml_file2, format_of_output='stylish') == expected_stylish_output
