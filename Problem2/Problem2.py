def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left, right, ret = 0, len(input_list) - 1, -1
    while left <= right:
        mid = int((left + right) / 2)

        if input_list[mid] == target:
            ret = mid
            break

        elif target < input_list[mid]:
            if target < input_list[left]:
                left = mid + 1
            else:
                right = mid - 1

        else:
            if target > input_list[right]:
                right = mid - 1
            else:
                left = mid + 1
    return ret


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    # print(rotated_array_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
