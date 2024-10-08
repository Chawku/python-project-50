import json
import pytest
from gendiff.generate_diff import generate_diff


def create_temp_json_file(content):
    with open("temp_file.json", "w") as f:
        json.dump(content, f)

def test_generate_diff():
    data1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    data2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }

    create_temp_json_file(data1)
    create_temp_json_file(data2)

    result = generate_diff("temp_file.json", "temp_file.json")
    expected_output = (
        "{\n"
        "  - follow: false\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: true\n"
        "}"
    )

    assert result.strip() == expected_output.strip()
    