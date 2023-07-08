import sys
N = int(sys.stdin.readline())
result_list=[]

for i in range(N):
    num = int(sys.stdin.readline())
    result_list.append(num)

result_list.sort()
for i  in result_list:
    print(i)
    