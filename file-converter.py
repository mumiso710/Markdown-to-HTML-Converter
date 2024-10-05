import sys
import markdown


def main():
    args = sys.argv[1:]
    if len(args) != 3:
        print_usage()
        return 1

    command = args[0]
    input_path = args[1]
    output_path = args[2]

    if command != "markdown":
        print_usage()
        return 1

    markdown.markdownFromFile(input=input_path, output=output_path)

    return 0


def print_usage():
    print("Usage: python3 file_converter.py markdown <input_path> <output_path>")


if __name__ == "__main__":
    main()
