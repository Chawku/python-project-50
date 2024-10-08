import json


def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    diff = []

    for key in all_keys:
        if key in data1 and key not in data2:
            diff.append(f"- {key}: {data1[key]}")
        elif key in data2 and key not in data1:
            diff.append(f"+ {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"- {key}: {data1[key]}")
            diff.append(f"+ {key}: {data2[key]}")

    return "{\n  " + "\n  ".join(diff) + "\n}"
