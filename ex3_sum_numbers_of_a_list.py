'''
PURPOSE:
3. Sum the numbers in a list (with reduce)
Create a function that, using reduce and a lambda function, takes a list of integers and returns the total sum of the numbers.
Example input: [1, 2, 3, 4]
Example output: 10
'''

from functools import reduce

def sum_integers(int_list: list) -> int:
    """Sums all integers in the given list.

    Args:
        int_list (list): A list of integers to be summed.

    Returns:
        int: The sum of all integers in the list.
    """
    accumulator = reduce(lambda x, y: x + y, int_list)
    return accumulator

int_list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 1024]

sum_total = sum_integers(int_list)

print(sum_total)