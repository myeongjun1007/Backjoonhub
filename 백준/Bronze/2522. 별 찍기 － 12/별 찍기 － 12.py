import sys
N = int(sys.stdin.readline())

for i in range(0,2*N-1):
    for j in range(0,2*N-1):
        if i<(2*N-1)//2:
            if j<(2*N-1)//2-i:
                print(" ",end="")
            elif ((2*N-1)//2-i <=j) and ((2*N-1)//2 >= j):
                print("*",end="")


        elif i>=(2*N-1)//2:
            if j< i-(2*N-1)//2:
                print(" ",end="")
            elif (i-(2*N-1)//2 <=j) and ((2*N-1)//2 >= j):
                print("*",end="")

    if i==2*N-2:
        continue
    else:
        print()