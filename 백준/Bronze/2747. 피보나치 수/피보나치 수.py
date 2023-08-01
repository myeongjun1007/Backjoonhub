import sys
N = int(sys.stdin.readline())
F0 = 0
F1 = 1
F_list = [0,1]

for i in range(2,N+1):
    F = F_list[i-1]+F_list[i-2]
    F_list.append(F)
    
print(F_list[-1])
