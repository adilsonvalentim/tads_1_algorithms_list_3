'''
PURPOSE:
Filter tuples with an average greater than 5
Write a function that receives a list of tuples, where each tuple contains integers. Use map and filter to filter the tuples whose average of the values is greater than 5.
Example input: [(2, 8), (4, 5, 6), (1, 2)]
Example output: [(2, 8), (4, 5, 6)]
'''

from functools import reduce

def filter_tuples_avg_higher_than_5(tuples_list: list) -> list:
    """
    Filters the tuples in list where the average of their elements is higher than 5.

    Args:
        tuples_list (list): A list of tuples, each containing integers values.

    Returns:
        list: List of tuples whose average is higher than 5.
    """
    avg_list = list(map(lambda x: (reduce(lambda y, z: y + z, x)) / len(x), tuples_list))
    
    filtered_tuple_list = list(filter(lambda x: avg_list[tuples_list.index(x)] > 5, tuples_list))
    
    return filtered_tuple_list

tuples_list = [(2, 8), (4, 5, 6), (1, 2), (2, 4, 5, 20), (5, 5, 5, 5, 5), (5, 5, 5, 5, 6)]

filtered_tuple_list = filter_tuples_avg_higher_than_5(tuples_list)

print(filtered_tuple_list)