from gendiff.cli import parsing_args
from gendiff.generate_diff import generate_diff


def main():
    args = parsing_args()

    diff = generate_diff(args.first_file, args.second_file,
                         format_of_output=args.format)
    print(diff)


if __name__ == '__main__':
    main()
