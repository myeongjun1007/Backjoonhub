import sys
N, M= map(int,sys.stdin.readline().split())
B_list = [i for i in range(1,N+1)]

for i in range(1,M+1):
    ith_input_list= list(map(int,sys.stdin.readline().split()))
    B_list[ith_input_list[0]-1] ,B_list[ith_input_list[1]-1] = \
    B_list[ith_input_list[1]-1], B_list[ith_input_list[0]-1]



print(*B_list)