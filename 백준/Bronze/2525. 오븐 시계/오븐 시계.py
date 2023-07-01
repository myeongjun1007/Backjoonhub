import sys
H, M = map(int,sys.stdin.readline().split())
time = int(sys.stdin.readline())

if M+time >= 60 :
    add_Hour = (M+time)//60
    H += add_Hour
    M = M+time-(60*add_Hour)
    if H >= 24:
        H -= 24
else :
    M = M+time
print(H,M)