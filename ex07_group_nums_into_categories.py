'''
PURPOSE:
7. Group numbers into categories (with dictionaries and lambdas)
Write a function that receives a list of integers and uses map and filter to create a dictionary that groups the numbers into three categories:

"positives" (numbers greater than 0)
"negatives" (numbers less than 0)
"zeros" (numbers equal to 0).
Example input: [1, -2, 0, 3, -5, 0]
Example output: {"positives": [1, 3], "negatives": [-2, -5], "zeros": [0, 0]}
'''

def categorizes_nums(nums_list: list) -> dict:
    """
    Categorizes integers in the list into positives, negatives and zeros in a dictionary.

    Args:
        nums_list (list): A list of integers to be categorized.

    Returns:
        dict: A dictionary with 3 Keys: "Positives" containing a list of positive numbers,
                "Negatives" containing a list of negative numbers, and "Zeros" containing
                a list of zeros.
    """
    positives = list(filter(lambda x: x > 0, nums_list))
    negatives = list(filter(lambda x: x < 0, nums_list))
    zeros = list(filter(lambda x: x == 0, nums_list))
    
    categorized_dict = {"Positives": positives, "Negatives": negatives, "Zeros": zeros}
    return categorized_dict

nums_list = [-20, 50, 1, -2, 0, 3, -5, 0, -50, 20]

categorized_dict = categorizes_nums(nums_list)

print(categorized_dict)


'''
#Alternative
def categorizes_nums(nums_list: list) -> dict:
    positives = []
    negatives = []
    zeros = []
    
    categories = list(map(lambda x: "positive" if x > 0 else ("negative" if x < 0 else "zero"), nums_list))
    
    categorized_dict = {
        "Positives": list(filter(lambda x: categories[nums_list.index(x)] == "positive", nums_list)),
        "Negatives": list(filter(lambda x: categories[nums_list.index(x)] == "negative", nums_list)),
        "Zeros": list(filter(lambda x: categories[nums_list.index(x)] == "zero", nums_list))
    }
    return categorized_dict
    '''