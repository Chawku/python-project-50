import pytest
from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1_path = "tests/fixtures/file1.json"
    file2_path = "tests/fixtures/file2.json"
    expected_output = (
        "{\n"
        "  - follow: False\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: True\n"
        "}"
    )

    result = generate_diff(file1_path, file2_path)

    assert result.strip() == expected_output.strip()
