#!/usr/bin/bash/python3
my_list = [1, 2, 3, 4, 5]
new_list = delete_at(my_list, 2)
print(new_list)  # Output: [1, 2, 4, 5]

new_list = delete_at(my_list, -1)
print(new_list)  # Output: [1, 2, 3, 4, 5]
