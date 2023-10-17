# This is my solution to Sofixit's Code Wars competition
# Test cases are located in 'main.py' file
# Maciej Kmieciak


def material(spaceship):
    # Check whether given argument is a list
    if isinstance(spaceship, list):

        # Check whether all elements of the list are integers
        if not all(isinstance(element, int) for element in spaceship):
            # Raise exception if not
            raise ValueError('material() error: not all elements of the list are integers')
    else:
        # Raise exception if not a list
        raise ValueError('material() error: argument is not a list')

    # Initialize material_amount - this is the number to be returned
    material_amount = 0

    # The length of the list for later multiple use
    len_spaceship = len(spaceship)

    # In case the list is empty, no material can be placed
    if len_spaceship == 0:
        return material_amount

    # Check whether all elements of the list are non-negative
    if min(spaceship) < 0:
        raise ValueError('material() error: elements of the list cannot be negative')

    max_level = max(spaceship)

    # For each horizontal level of given spaceship,
    # up to the highest level which still has boxes
    for current_level in range(1, max_level + 1):

        left_index_limit = None
        right_index_limit = None

        # Find the left index limit for current level
        # i.e. the first element in the list,
        # which is bigger than or equal to the current level.
        for i in range(len_spaceship):
            if spaceship[i] >= current_level:
                left_index_limit = i
                break

        # Similarly for the right index limit
        for i in range(len_spaceship):
            if spaceship[len_spaceship - (i + 1)] >= current_level:
                right_index_limit = len_spaceship - (i + 1)
                break

        # Fill all the empty space in between with material
        # on the current level, except the space taken by boxes.
        # In case there is no such range,
        # the loop will not be executed even once.
        for i in range(left_index_limit + 1, right_index_limit):
            if spaceship[i] < current_level:  # Check if the space is taken by a box.
                material_amount += 1

    # At this point all possible levels to fill have been covered
    return material_amount

