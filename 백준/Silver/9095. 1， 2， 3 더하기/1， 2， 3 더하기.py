import sys


def sum_fn(n):
    if n==1:
        return 1

    elif n==2:
        return 2

    elif n==3:
        return 4
    else:
        return sum_fn(n-1) + sum_fn(n-2) + sum_fn(n-3)


T = int(sys.stdin.readline())
for i in range(T):
    num = int(sys.stdin.readline())
    print(sum_fn(num))
