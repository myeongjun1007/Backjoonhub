import sys
N = int(sys.stdin.readline())

time_list = []
time_cnt = 1

for i in range(N):
    start,end = map(int,sys.stdin.readline().split())
    time_list.append([start,end])



time_list.sort(key=lambda x : (x[1],x[0]))

begin_time = time_list[0][1]


for time in time_list[1:]:
    if time[0] <= time[1]:
        if time[0] >= begin_time:

            time_cnt += 1
            begin_time = time[1]


print(time_cnt)
