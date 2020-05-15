from Utilities import partition


def q_sort_iteration(arr, low, high):
    if low >= high:
        return
    regions = [[low, high]]
    i = 0
    while i < len(regions):
        low = regions[i][0]
        high = regions[i][1]
        p = partition(arr, low, high)
        if p != -1:
            regions.append([low, p - 1])
            regions.append([p + 1, high])
        i += 1
    return


# 下面是调用代码，在书中应该独立形成一个代码块

arr = [2, 1, 5, 8, 7, 13, 26, 4, 39, 0]
q_sort_iteration(arr, 0, len(arr) - 1)
print(arr)
