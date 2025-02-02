'''
PURPOSE:
2. Filter even numbers from a list (using filter)
Write a function that, using filter and a lambda function, takes a list of integers and returns only the even numbers.
Example input: [1, 2, 3, 4, 5]
Example output: [2, 4]
'''

def even_numbers_filter(numbers_list: list) -> list:
    """
    Filter even numbers in an integer list.

    Filter even numbers in an integer list via filter and lambda,
    then returns the even numbers list.

    Args:
        numbers_list (list): List containing integer numbers that will be filtered.

    Returns:
        list: List containing the filtered result containing only the even integer numbers of the original list.
    """
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
    return even_numbers

numbers_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

even_numbers = even_numbers_filter(numbers_list)

print(even_numbers)