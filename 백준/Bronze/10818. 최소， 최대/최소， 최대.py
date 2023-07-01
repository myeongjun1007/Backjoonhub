import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

max = lst[0]
min = lst[0]


for i in lst:
    if i < min:
        min = i
    if i > max:
        max = i


print(f"{min} {max}")