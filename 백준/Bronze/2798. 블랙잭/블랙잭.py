import sys
N , M = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))


diff_min = M
result = 0
for i in num_list:
    for j in num_list:
        if j != i:
            for k in num_list:
                if ( k != i) and (k != j):
                    temp_sum = i + j + k
                    temp_diff = M - temp_sum
                
                    if  0 <= temp_diff < diff_min:
                        diff_min = temp_diff
                        result = temp_sum
              
                 

                else:
                    continue
        else:
            continue

print(result)
