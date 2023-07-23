import sys
N = int(sys.stdin.readline())
size_list =[]
for i in range(N):
    weight, height = map(int,sys.stdin.readline().split())
    size_list.append([weight,height])

rank_list = [1 for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j :
            continue

        elif (size_list[i][0] < size_list[j][0]) and (size_list[i][1] < size_list[j][1]):
            rank_list[i] += 1

print(*rank_list)
