import os
import pytest
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


def test_generate_diff_yaml(load_file_content):
    file1 = os.path.join("tests", "fixtures", "file1.yaml")
    file2 = os.path.join("tests", "fixtures", "file2.yaml")

    expected_output = load_file_content("expected_stylish_output.txt")

    result = generate_diff(file1, file2, format_of_output='stylish')

    assert result == expected_output
