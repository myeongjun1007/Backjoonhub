import sys
N = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
target_num = int(sys.stdin.readline())

cnt=0
for i in num_list:

    if i==target_num:
        cnt+=1

print(cnt)