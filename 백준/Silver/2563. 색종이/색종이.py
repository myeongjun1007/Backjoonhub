import sys
from pprint import pprint
N = int(sys.stdin.readline())

canvas =[[0 for _ in range(0,100)]for _ in range(0,100)]

for page in range(0,N):
    width_start, height_start = map(int,sys.stdin.readline().split())
    for i in range(100-height_start-10,100-height_start):
        for j in range(width_start,width_start+10):


            if canvas[i][j] == 0:
                canvas[i][j] = 1


sum=0
for i in range(0,100):
    for j in range(0,100):
        sum += canvas[i][j]


print(sum)