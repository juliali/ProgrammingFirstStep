def closest_sqrt(n):
    if n <= 0:
        print("input number is not invalid")
        return -1
    low = 1
    high = n
    while low <= high:
        m = int((high - low) / 2) + low
        if m * m == n:
            return m
        elif m * m < n < (m + 1) * (m + 1):
            if n - m * m > (m + 1) * (m + 1) - n:
                return m + 1
            else:
                return m
        else:
            if m * m > n:
                high = m - 1
            else:
                low = m + 1
    return -1


# 下面代码为调用上面函数，应添加入原文，成为独立代码块

for i in range(1, 101):
    print(i, closest_sqrt(i))
