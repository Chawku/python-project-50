import os
import pytest
import json
from gendiff.generate_diff import make_diff, build_diff, generate_diff


@pytest.fixture
def fixture_path():
    return os.path.join("tests", "fixtures")


@pytest.fixture
def load_file_content(fixture_path):
    def _load_file(filename):
        file_path = os.path.join(fixture_path, filename)
        with open(file_path, 'r') as f:
            return f.read()
    return _load_file


def test_make_diff(load_file_content):
    dict1 = json.loads(load_file_content("file1.json"))
    dict2 = json.loads(load_file_content("file2.json"))
    expected = json.loads(load_file_content("expected_make_diff.txt"))

    assert make_diff(dict1, dict2) == expected


def test_build_diff(load_file_content):
    dict1 = json.loads(load_file_content("file1.json"))
    dict2 = json.loads(load_file_content("file2.json"))
    expected = json.loads(load_file_content("expected_build_diff.txt"))

    assert build_diff(dict1, dict2) == expected


def test_generate_diff(load_file_content):
    file1 = os.path.join("tests", "fixtures", "file1.json")
    file2 = os.path.join("tests", "fixtures", "file2.json")
    expected_stylish_output = load_file_content("expected_stylish_output.txt")

    assert generate_diff(file1, file2, format_of_output='stylish') == expected_stylish_output
