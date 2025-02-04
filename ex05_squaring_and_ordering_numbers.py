'''
PURPOSE:
5. Square numbers and sort (with map and sorted)
Create a function that squares all the numbers in a list, using map, and then returns the sorted list.
Example input: [3, 1, 4, 2]
Example output: [1, 4, 9, 16]
'''

def squaring_and_ordering(nums_list: list) -> list:
    """
    Squares each number in a list and returns them in ascending order.

    Args:
        nums_list (list): A list of float numbers to be squared and ordered.

    Returns:
        list: The list of squared numbers sorted in ascending order.
    """
    squared_and_ordered = sorted(list(map(lambda x: round(x ** 2, 2), nums_list)))
    return squared_and_ordered

nums_list = [-2.4, 6, -1, 0.1, 2, 3.2, -9.9, 4, 2.3]

squared_and_ordered = squaring_and_ordering(nums_list)

print(squared_and_ordered)