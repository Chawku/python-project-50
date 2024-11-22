import os
import pytest
import json
from gendiff.formatters.plain import format_diff


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


def test_format_diff_plain(load_file_content):
    diff_file = os.path.join("tests", "fixtures", "diff.json")
    expected_output = load_file_content("expected_plain_output.txt")
    
    with open(diff_file, 'r') as f:
        diff = json.load(f)

    result = format_diff(diff)

    assert result == expected_output
