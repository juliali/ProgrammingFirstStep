from Utilities import swap


def bubble_sort(arr):

    for i in range(0, len(arr) - 1):
        swapped = False

    for j in range(len(arr) -1, i, -1):
        if arr[j] <arr[j - 1]:
            swap(arr, j, j-1)
            swapped = True

    if not swapped:
        return

    return