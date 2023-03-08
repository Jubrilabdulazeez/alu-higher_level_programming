#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list from which an item is to be deleted.
        idx (int): The index of the item to be deleted.

    Returns:
        list: The updated list after deleting an item at the specified index.
    """
    # If the list is empty, return it as it is
    if not my_list:
        return my_list

    # If the index is negative or out of range, return the original list
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Copy the list
    new_list = my_list[:]

    # Delete the item at the specified index
    del new_list[idx]

    return new_list
