import sys
N,M = map(int,sys.stdin.readline().split())
matA = []
matB = []
matC = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    temp_row = list(map(int,sys.stdin.readline().split()))
    matA.append(temp_row)

for i in range(N):
    temp_row = list(map(int,sys.stdin.readline().split()))
    matB.append(temp_row)


for row in range(N):
    for col in range(M):
        matC[row][col] = matA[row][col] + matB[row][col]

        print(matC[row][col], end=" ")

    if row==N-1:
        continue

    print()