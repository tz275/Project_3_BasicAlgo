def sort_012(lst):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Initialize counters for 0, 1, and 2
    zero_count = 0
    one_count = 0
    two_count = 0

    # Count the number of 0s, 1s, and 2s in the list
    for num in lst:
        if num == 0:
            zero_count += 1
        elif num == 1:
            one_count += 1
        elif num == 2:
            two_count += 1

    # Replace the elements in the list with the appropriate number of 0s, 1s, and 2s
    lst[:zero_count] = [0] * zero_count
    lst[zero_count:zero_count + one_count] = [1] * one_count
    lst[zero_count + one_count:] = [2] * two_count
    return lst

print(sort_012([1,2,2,2]))


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