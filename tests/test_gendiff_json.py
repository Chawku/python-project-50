import os
import pytest
import json
from gendiff.generate_diff import generate_diff


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


def test_generate_diff_json(load_file_content):
    file1 = os.path.join("tests", "fixtures", "file1.json")
    file2 = os.path.join("tests", "fixtures", "file2.json")
    
    expected_output = json.loads(load_file_content("expected_output.txt"))

    result = json.loads(generate_diff(file1, file2, format_of_output='json'))

    assert result == expected_output
