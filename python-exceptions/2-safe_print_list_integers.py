#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if isinstance(i, int):
                print("{:d}".format(i), end=" ")
                count += 1
        except:
            pass
        if count == x:
            break
    print()  # add a newline after printing all integers
    return count
