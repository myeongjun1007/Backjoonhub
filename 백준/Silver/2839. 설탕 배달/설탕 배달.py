import sys
N = int(sys.stdin.readline())
cnt_5 = 0
cnt_3 = 0
min_cnt = 1666
answer_list =[]

for i in range(N//5 + 1):
    for j in range(N//3 + 1):
        # print(i , j , cnt_5, cnt_3)


        if (i*5+j*3==N):
            cnt_5 = i
            cnt_3 = j
            temp_cnt = cnt_5 + cnt_3
            answer_list.append(temp_cnt)
            # print(temp_cnt)
            if  temp_cnt < min_cnt:
                min_cnt = temp_cnt

if len(answer_list)==0:
    print(-1)

else:
    print(min_cnt)