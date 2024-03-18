import pandas as pd


def input_text():
    """
    Function to input text from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")


def read_from_file(filename):
    """
    Function to read from a file using Python's built-in capabilities.

    Parameters:
        filename (str): The path to the file to be read.

    Returns:
        str or None: The content of the file or None if the file was not found.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found.")
        return None


def read_with_pandas(filename):
    """
    Function to read from a file using the pandas library.

    Parameters:
        filename (str): The path to the file to be read.

    Returns:
        pandas.DataFrame or None: DataFrame if the data was successfully read, or None if the file was not found.
    """
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None
