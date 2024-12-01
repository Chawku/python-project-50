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


@pytest.mark.parametrize(
    "file1, file2, expected_file, format_of_output",
    [
        ("file1.json", "file2.json", "expected_output.txt", "json"),
        ("file1.yaml", "file2.yaml", "expected_stylish_output.txt", "stylish"),
        (
            "file1_tree.json",
            "file2_tree.yaml",
            "expected_tree_stylish_output.txt",
            "stylish",
        ),
        (
            "file1_tree.json",
            "file2_tree.yaml",
            "expected_plain_output.txt",
            "plain",
        ),
    ],
)
def test_generate_diff(
    file1, file2, expected_file, format_of_output,
    load_file_content, fixture_path
):
    file1_path = os.path.join(fixture_path, file1)
    file2_path = os.path.join(fixture_path, file2)
    expected_output = load_file_content(expected_file)

    result = generate_diff(file1_path, file2_path,
                           format_of_output=format_of_output)

    assert ''.join(result.split()) == ''.join(expected_output.split())
