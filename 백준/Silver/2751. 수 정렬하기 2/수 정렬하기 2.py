N = int(input())
result_list = []

for i in range(N):
    value = int(input())
    result_list.append(value)

result_list.sort()

for value in result_list:
    print(value)