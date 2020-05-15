def recursion_test(depth):
    if depth <1000:
        recursion_test(depth + 1)
    return

# 下面为调用代码，应形成独立代码块

recursion_test(1)