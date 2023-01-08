def quickSelect(lst, index):
    if not lst:
        return None
    pivot = lst[-1]
    left = [x for x in lst if x < pivot]
    right = [x for x in lst if x > pivot]
    if index <= len(left):
        return quickSelect(left, index)
    elif index == len(left) + 1:
        return pivot
    else:
        return quickSelect(right, index - len(left) - 1)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    ret1, ret2 = [], []
    for i in range(1, len(input_list) + 1)[::-1]:
        if i % 2 == 0:
            ret1.append(str(quickSelect(input_list, i)))
        else:
            ret2.append(str(quickSelect(input_list, i)))
    ret1 = ''.join(ret1)
    ret2 = ''.join(ret2)
    ret = [int(ret1), int(ret2)]
    return ret




def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

