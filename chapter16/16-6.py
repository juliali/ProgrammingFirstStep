def fibonacci(n):
    if n <0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 下面为调用代码，应形成独立代码块

print(fibonacci(10))