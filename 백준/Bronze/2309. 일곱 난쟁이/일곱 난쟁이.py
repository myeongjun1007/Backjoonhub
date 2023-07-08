import sys
tall_list=[]
tall_sum = 0

for i in range(9):
    tall = int(sys.stdin.readline())
    tall_list.append(tall)
    tall_sum += tall

tall_list.sort()

first_index = 0
second_index = 0

flag = False
for i in range(9):
    for j in range(9):
        if (i != j):
            if (tall_sum - tall_list[i] - tall_list[j]) == 100:
                first_index = i
                second_index = j

                flag = True
                break

    if flag:
        break

for i in range(9):
    if (i==first_index) or (i==second_index):
        continue

    else :
        print(tall_list[i])
        