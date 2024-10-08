import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file",
                        help="Path to the first configuration file")
    parser.add_argument("second_file",
                        help="Path to the second configuration file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        choices=['plain', 'json'],
        default='plain'
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
