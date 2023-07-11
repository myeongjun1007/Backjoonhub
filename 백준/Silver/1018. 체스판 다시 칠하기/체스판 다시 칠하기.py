import sys
from pprint import pprint
N, M = map(int,sys.stdin.readline().split())

min_change_cnt =64

input_list=[]
for a in range(0,N):
    input_row = list(input())
    input_list.append(input_row)



total=0
total1 = 64
total2 = 64
for i in range(0,(N+1)-8):
    for j in range(0,(M+1)-8):

        temp_chess=[[0 for _ in range(8)]for _ in range(8)]


        for row in range(0,8):
            for col in range(0,8):
                temp_chess[row][col]=input_list[i+row][j+col]

        change_cnt = 0
        # if temp_chess[0][0] == 'B':
        for a in range(0,8):
            for b in range(0,8):
                if (a+b)%2 ==0:
                    if temp_chess[a][b] !='B':
                        # temp_chess[a][b] ='B'
                        change_cnt += 1


                elif (a+b)%2 ==1:
                    if temp_chess[a][b] !='W':
                        # temp_chess[a][b] ='W'
                        change_cnt += 1

        total1 = min(change_cnt,min_change_cnt,total2)
        # if temp_chess[0][0] == 'W':
        change_cnt = 0
        for a in range(0,8):
            for b in range(0,8):
                if (a+b)%2 ==0:
                    if temp_chess[a][b] !='W':
                        # temp_chess[a][b] ='W'
                        change_cnt += 1



                elif (a+b)%2 == 1:
                    if temp_chess[a][b] !='B':
                        # temp_chess[a][b] ='B'
                        change_cnt += 1

        total2 = min(change_cnt, min_change_cnt,total1)

        total = min(total1,total2)



print(total, end='')
