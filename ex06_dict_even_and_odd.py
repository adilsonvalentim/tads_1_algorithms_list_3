'''
PURPOSE:
6. Dictionary of even and odd numbers
Write a function that receives a list of integers and uses lambda and filter to split the list into even and odd numbers. Return a dictionary with two keys: "even" and "odd".
Example input: [1, 2, 3, 4, 5, 6]
Example output: {"even": [2, 4, 6], "odd": [1, 3, 5]}
'''

def dict_even_and_odd(int_list: list) -> dict:
    """
    Separates the integers in a list into a dictionary of even and odd numbers.

    Args:
        int_list (list): A list of integers to be separated in even and odd.

    Returns:
        dict: A dictionary with two keys: "Even" containing a list of even numbers,
                and "Odd" contaning a list of odd numbers.
    """
    even = list(filter(lambda x: x % 2 == 0, int_list))
    odd = list(filter(lambda x: x % 2 == 1, int_list))
    
    separated_dict = {"Even": even, "Odd": odd}
    return separated_dict

int_list = [-12, -5, -2, 0, 1, 4, 7, 10, 15]

separated_dict = dict_even_and_odd(int_list)

print(separated_dict)