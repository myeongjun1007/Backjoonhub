import sys
N, M= map(int,sys.stdin.readline().split())
B_list = [0 for i in range(0,N)]

for i in range(1,M+1):
    ith_input_list= list(map(int,sys.stdin.readline().split()))
    for j in range(ith_input_list[0],ith_input_list[1]+1):
        B_list[j-1]=ith_input_list[2]

print(*B_list)