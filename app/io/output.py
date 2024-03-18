def output_to_console(text):
    """
    Function to output text to the console.

    Parameters:
        text (str): The text to be printed to the console.

    Returns:
        None
    """
    print(text)


def write_to_file(filename, content):
    """
    Function to write content to a file using Python's built-in capabilities.

    Parameters:
        filename (str): The path to the file to write to.
        content (str): The content to be written to the file.

    Returns:
        None
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
    except Exception as e:
        print("Error occurred while writing to the file:", e)
