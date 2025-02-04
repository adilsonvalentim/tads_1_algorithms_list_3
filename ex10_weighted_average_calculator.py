'''
PURPOSE:
10. Weighted Average with Dictionary and Reduce
Create a function that receives a dictionary where the keys are student names and the values are lists of grades (with weights in the last position). The function should calculate the weighted average of each student using reduce and return a new dictionary with the results.
Example input:
{
    "João": [8, 7, 9, (1, 2, 3)],  # (grades: 8, 7, 9; weights: 1, 2, 3)
    "Ana": [5, 6, 7, (3, 1, 2)]    # (grades: 5, 6, 7; weights: 3, 1, 2)
}

Example output:
{
    "João": 8.0,
    "Ana": 6.0
}
'''

from functools import reduce

def weighted_avg_calculator(student_grades: dict) -> dict:
    """
    Calculate the weighted average for each student based on their grades
    and corresponding weights.

    Args:
        student_grades (dict): A dictionary where the keys are the student
            names and the values are lists containing the grades and the last
            element containing a tuple with the weights of each grade.

    Returns:
        dict: A dictionary with student names as keys and their respective weighted average grade.
    """
    weights = list(map(lambda grades: list(grades.pop()), student_grades.values()))
    
    sum_of_weights = list(map(lambda sublist: reduce(lambda x, y: x + y, sublist), weights))
    
    weighted_grades = list(map(lambda grades, weights: [grade * weight for grade, weight in zip(grades, weights)], student_grades.values(), weights))
    
    sum_of_wgh_grades = list(map(lambda sublist: reduce(lambda x, y: x + y, sublist), weighted_grades))
    
    weighted_avg_grades_dict = dict(map(lambda keys, s_grades, s_weights: (keys, round((s_grades / s_weights), 2)), student_grades.keys(), sum_of_wgh_grades, sum_of_weights))
    
    return weighted_avg_grades_dict

student_general_grades = {
"John": [8, 7, 9, 10, 10, 10, 0, (1, 2, 3, 5, 4, 6, 10)],
"Anna": [5, 6, 7, (3, 1, 2)],
"Dean": [10, 8, 2, (1, 3, 2)],
"Sam": [4, 2, 10, (3, 2, 1)],
"Peter": [8, 8, 8, (2, 1, 3)]
}
weighted_avg_grades_dict = weighted_avg_calculator(student_general_grades)
print(weighted_avg_grades_dict)