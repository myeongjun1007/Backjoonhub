import sys
N = int(sys.stdin.readline())

Q = N // 4
R = N % 4
if R > 0:
    for i in range(1,Q+2):
        print("long",end=" ")
    print("int")
else:
    for i in range(1,Q+1):
        print("long",end=" ")
    print("int")