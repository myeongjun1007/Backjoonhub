import sys
A,B,C = map(int,sys.stdin.readline().split())

time_list = []

for i in range(3):
    time = list(map(int,sys.stdin.readline().split()))
    time_list.append(time)

max_end = max(time_list[0][1], time_list[1][1],time_list[2][1])


cnt_list = [0 for i in range(max_end)]

for time_range in time_list:
    for i in range(time_range[0], time_range[1]):
        cnt_list[i] += 1

fee=0
for i in cnt_list[1:]:
    if i == 1:
        fee += A*1

    elif i == 2:
        fee += B*2

    elif i == 3:
        fee += C*3

print(fee)