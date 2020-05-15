from Utilities import partition_v2
from Utilities import generate_test_data


def qsort_recursion_v2(arr, low, high):
    if low >= high:
        return

    p = partition_v2(arr, low, high) #调用新的分区函数
    qsort_recursion_v2(arr, low, p - 1)
    qsort_recursion_v2(arr, p + 1, high)

    return

# 下面为代码16-12
_, _, arr_reverse = generate_test_data(1, 1000)

# 下面一行为打印提示语句，不要出现在代码示例里：
print("\n\nFollowing are output of code 16-13\n")

# 下面为代码16-13
qsort_recursion_v2(arr_reverse, 0, len(arr_reverse) - 1)
print("sorted :", arr_reverse)

# 下面一行为打印提示语句，不要出现在代码示例里：
print("\n\nFollowing are output of code 16-14\n")

# 下面为代码16-14
_, _, arr_reverse = generate_test_data(1, 2000)
qsort_recursion_v2(arr_reverse, 0, len(arr_reverse) - 1)
print("sorted arrReverse:",arr_reverse)