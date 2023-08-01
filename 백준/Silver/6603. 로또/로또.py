import sys

def pick_lotto(depth,start_idx,lotto_list):

    global K
    global pick_list


    if depth == 6:
        print(*pick_list)
        return


    for idx in range(start_idx,len(lotto_list)):
        pick_list[depth] = lotto_list[idx]
        pick_lotto(depth+1,idx+1,lotto_list)




flag = False
while not flag:
    test_case = list(map(int,(sys.stdin.readline().strip().split())))
    if test_case[0] == 0:
        flag = True
        break
    else:
        K = test_case[0]
        lotto_list = sorted(test_case[1:])
        pick_list = [0 for _ in range(6)]

        pick_lotto(0,0,lotto_list)
    print()