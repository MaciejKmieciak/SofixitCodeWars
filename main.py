# This is my solution to Sofixit's Code Wars competition
# The function itself is located in 'material.py' file
# Maciej Kmieciak

from material import material

test_cases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2],
    [4, 2, 0, 3, 2, 5],
    [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3],
    [6, 2, 1, 1, 8, 0, 5, 5, 0, 1, 8, 9, 6, 9, 4, 8, 0, 0],
    [2, 0, 0, 2, 0, 1, 0],
    [8, 0, 2, 1, 2, 0, 8, 1],
    [2, 0, 1, 3, 2, 3],
    [0, 1, 0, 0],
    [3, 3, 3],
    [2],
    [0, 0, 0],
    [0],
    [],
    'xyz',
    [1, 2, 'abc'],
    [1, 0, 2, -3]
]

print("This is my solution to Sofixit's Code Wars competition")
print("The function itselt is located in 'material.py' file")
print("Maciej Kmieciak")
print()

for test_case in test_cases:
    print("Test case:", test_case)
    try:
        print("Result:", material(test_case))
    except ValueError as my_value_error:
        print(my_value_error)
    print()
