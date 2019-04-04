#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # If the index is equal to the array
    # Which mean that the program has gone through the array but haven't found the item
    array_length = len(array)
    if index == array_length:
        return None

    if array[index] != item:
        return linear_search_recursive(array, item, index + 1)
    else:
        return index


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    starting_point = 0
    end_point = len(array) - 1

    while end_point >= starting_point:
        # The middle index of the array if the average of two end points
        middle_index = int((starting_point + end_point) / 2)

        # Did not found the item in the array
        # if middle_index == 0:
        #     return None
        # Check if the middle index is the item first
        if array[middle_index] == item:
            return middle_index

        # The item of the middle index is larger in ascii value
        elif array[middle_index] > item:
            end_point = middle_index - 1

        # The item of the middle index is less in ascii value
        elif array[middle_index] < item:
            starting_point = middle_index + 1

        else:
            return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

    # Getting the middle index of the array

    if left == None:
        left = 0

    if right == None:
        right = len(array) -1


    if right >= left:
        middle_index = int((left + right) / 2)

        if array[middle_index] == item:
            return middle_index

        elif array[middle_index] > item:
            return binary_search_recursive(array, item, left, middle_index - 1)
        else:
            return binary_search_recursive(array, item, middle_index + 1, right)
    else:
        return None


names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
print(binary_search(names, 'Kojin'))
