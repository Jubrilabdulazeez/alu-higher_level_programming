#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]

# Remove the item at index 2
new_list = delete_at(my_list, 2)
print(new_list)  # Output: [1, 2, 4, 5]

# Remove the item at index -1 (which is out of range)
new_list = delete_at(my_list, -1)
print(new_list)  # Output: [1, 2, 3, 4, 5]
