import sys
from collections import deque

T = int(sys.stdin.readline())

direction_x = [0,0,1,-1]
direction_y = [1,-1,0,0]
def bfs(field,row,col):
    que = deque()
    que.append((row,col))
    field[row][col] = 0

    while que:
        curr_x, curr_y = que.popleft()

        for l in range(4):
            next_x = curr_x + direction_x[l]
            next_y = curr_y + direction_y[l]

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue

            if field[next_x][next_y] == 1:
                field[next_x][next_y] = 0
                que.append((next_x,next_y))

    return



for i in range(T):
    cnt = 0
    n, m, k = map(int,sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]

    for j in range(k):
        x,y = map(int,sys.stdin.readline().split())
        field[x][y] =1

    for a in range(n):
        for b in range(m):
            if field[a][b] == 1:
                bfs(field, a, b)

                cnt += 1

    print(cnt)
