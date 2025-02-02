'''
PURPOSE:
8. Count letters in a list of words (with map and reduce)
Create a function that receives a list of words and returns the total sum of letters in all the words, using map to count the letters and reduce to sum them.
Example input: ["casa", "python", "lambda"]
Example output: 16
'''
from functools import reduce

def letters_counter_in_list(words_list: list) -> int:
    """
    Counts the total of letters in all words in a list.

    Args:
        words_list (list): A list of words to have their letters counted.

    Returns:
        int: The total number of letters in all the words in the given list.
    """
    number_of_letters_list = list(map(lambda x: len(x), words_list))
    
    total_of_letters = reduce(lambda x, y: x + y, number_of_letters_list)
    
    return total_of_letters

words_list = ["casa", "python", "lambda", "constitucionalicimamente"]

total_of_letters = letters_counter_in_list(words_list)

print(total_of_letters)