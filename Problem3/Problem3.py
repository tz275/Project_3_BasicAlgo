def partitioning(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partitioning(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def rearrange_digits(input_list=None):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return []
    quickSort(input_list, 0, len(input_list) - 1)
    ret1, ret2 = [], []
    for i in range(0, len(input_list))[::-1]:
        if i % 2 == 0:
            ret1.append(str(input_list[i]))
        else:
            ret2.append(str(input_list[i]))
    ret1 = ''.join(ret1)
    ret2 = ''.join(ret2)
    ret = [int(ret1), int(ret2)]
    return ret


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Edged Test Cases
print(rearrange_digits([]))
print(rearrange_digits())
