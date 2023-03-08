#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a list of True or False values indicating whether each integer in the input list is a multiple of 2.
    """
    # Initialize an empty list to store the results
    results = []

    # Iterate through the input list
    for num in my_list:
        # Check if the current number is divisible by 2
        if num % 2 == 0:
            results.append(True)
        else:
            results.append(False)

    # Return the list of results
    return results
