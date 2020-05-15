def recursion_test(depth):
    print("recursion depth:", depth)
    if depth < 996:
        recursion_test(depth + 1)
    else:
        print("exit recursion")
    return

# 下面为调用代码，应形成独立代码块

recursion_test(1)