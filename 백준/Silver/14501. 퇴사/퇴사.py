import sys
N = int(sys.stdin.readline())

counsel_list = [[0,0]]
for i in range(1,N+1):
    input = list(map(int,sys.stdin.readline().split()))
    counsel_list.append(input)

max_sum = 0
final_work = [0 for _ in range(N+1)]
time_list = [i[0] for i in counsel_list]
pay_list = [i[1] for i in counsel_list]
# 
# print(time_list)
# print(pay_list)
def retire_work(day,target_list):

    global max_sum
    global final_work,time_list, pay_list

    # print(f"day : {day}")
    # print(f'max_sum : {max_sum}')
    if day > N :
        # print("update 실행")
        # print(f"final_work : {final_work}")
        temp_sum = sum(final_work)

        if temp_sum >= max_sum:
            max_sum = temp_sum

        return

    for idx in range(day,len(target_list)):
        need_time = time_list[idx]
        earn_pay = pay_list[idx]
        if idx + need_time <= len(target_list):
            final_work[idx] = earn_pay

        retire_work(idx+need_time, target_list)
        final_work[idx] = 0




retire_work(1,counsel_list)

print(max_sum)