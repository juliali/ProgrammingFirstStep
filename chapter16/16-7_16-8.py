from Utilities import partition


def qsort_recursion(arr, low, high):
    if low >= high:
        return
    p = partition(arr, low, high)
    qsort_recursion(arr, low, p - 1)
    qsort_recursion(arr, p + 1, high)
    return


# 下面是16-8
arr = [7, 9, 6, 8, 10, 3, 2, 1, 4, 5]
qsort_recursion(arr, 0, len(arr) - 1)
print(arr)
