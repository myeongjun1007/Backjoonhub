import sys
N = int(sys.stdin.readline())
Target = int(sys.stdin.readline())
Target_position = []
height = 0
width = 0

snail_list = [[0 for _ in range(N)] for _ in range(N)]

num_now = N*N
cnt = 1

snail_list[0][0] = N*N

for i in range(0,N//2):
    for k in range(1,(N-2*i)*(N-2*i)-(N-2*(i+1))*(N-2*(i+1))+1):
        cnt += 1
        num_now -= 1
        if k <= ((N-2*i)-1):
            height += 1
            snail_list[height][width] = num_now

        elif k<= 2*((N-2*i)-1):
            width += 1
            snail_list[height][width] = num_now

        elif k <= 3*((N-2*i)-1):
            height -= 1
            snail_list[height][width] = num_now

        elif k <= 4*((N-2*i)-1) -1 :
            width -= 1
            snail_list[height][width] = num_now

        else :
            height += 1
            snail_list[height][width] = num_now



for i in range(N):
    for j in range(N):
        print(snail_list[i][j] , end=" ")
        if snail_list[i][j] == Target:
            Target_position.append(i+1)
            Target_position.append(j+1)

    if i == N-1:
        print()
        print(*Target_position)



    else:
        print()
