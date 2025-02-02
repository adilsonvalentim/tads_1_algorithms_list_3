'''
PURPOSE:
4. Names with more than 5 letters (with filter)
Write a function that takes a list of names and, using filter, returns only the names with more than 5 letters.
Example input: ["Ana", "Lucas", "Fernanda", "João"]
Example output: ["Lucas", "Fernanda"]
'''

def more_than_5_chars_filter(name_list: list) -> list:
    """Filters the names that have more than 5 characters in a list.

    Args:
        name_list (list): A list of names to be filtered.

    Returns:
        list: A list of names that have more than 5 characters.
    """
    more_than_5_chars_list = list(filter(lambda x: len(x) > 5, name_list))
    return more_than_5_chars_list

name_list = ["Neymar", "Adilson", "Ronaldinho", "Kaká", "Dunga", "Taffarel", "Zuckerberg", "Chapolin", "Nosferatu", "Itachi"]

more_than_5_chars_list = more_than_5_chars_filter(name_list)

print(more_than_5_chars_list)