import math


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None
    s, l = math.inf, math.inf * -1
    for i in ints:
        if type(i) is not int:
            raise Exception("Wrong input type!")
        if i < s:
            s = i
        if i > l:
            l = i
    return (s, l)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Edged Test Cases
print("Pass" if get_min_max([]) is None else "Fail")

try:
    get_min_max(['a'])
except:
    print("Pass")

