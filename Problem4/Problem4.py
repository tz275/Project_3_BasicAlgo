def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return


def sort_012(lst):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       lst(list): List to be sorted
    """
    if not lst:
        raise Exception("Input is None")

    i_0, i_1, i_2 = 0, 0, len(lst) - 1
    while i_1 <= i_2:
        m = lst[i_1]
        if m not in [0, 1, 2]:
            raise Exception("Wrong Value in the Given List!")
        if m == 0:
            swap(lst, i_0, i_1)
            i_0 += 1
            i_1 += 1
        elif m == 1:
            i_1 += 1
        else:
            swap(lst, i_1, i_2)
            i_2 -= 1
    return lst


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edged Test Cases:
try:
    sort_012([1, 2, 3, 4, 5, 6])
    print("Fail")
except:
    print("Pass")

try:
    sort_012([])
    print("Fail")
except:
    print("Pass")


