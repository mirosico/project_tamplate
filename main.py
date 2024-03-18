from app.io.input import input_text, read_from_file, read_with_pandas
from app.io.output import output_to_console, write_to_file


def main():
    text_from_console = input_text()
    text_from_file = read_from_file("data/read_data.txt")
    text_from_file_red_by_pandas = read_with_pandas("data/read_data.txt")

    output_to_console(text_from_console)
    output_to_console(text_from_file_red_by_pandas)
    output_to_console(text_from_file)

    write_to_file("data/target_file.txt", text_from_file)


if __name__ == '__main__':
    main()
