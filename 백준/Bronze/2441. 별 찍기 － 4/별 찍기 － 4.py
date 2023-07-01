import sys
N = int(sys.stdin.readline())

for i in range(N):
    for j in range(i):
        print(' ',end='')

    print('*'*(N-i),end="")
    print(" ")
