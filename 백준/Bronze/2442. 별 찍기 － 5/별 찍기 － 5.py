import sys
N = int(sys.stdin.readline())

for i in range(N):
    print(" "*((2*N-1)//2-i),end='')
    print("*"*(2*i+1),end='')

    if i==N-1:
        continue
    else:
        print()