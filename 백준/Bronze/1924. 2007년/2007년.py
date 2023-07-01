import sys
x , y = map(int,sys.stdin.readline().split())

day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
if x==1:
    print(day[(y-1)%7])

elif x==2:
    print(day[(31+y-1)%7])

elif x==3:
    print(day[(31+28 + y - 1) % 7])

elif x==4:
    print(day[(31+28+31 + y - 1) % 7])

elif x==5:
    print(day[(31+28+31+30 + y - 1) % 7])

elif x==6:
    print(day[(31+28+31+30+31 + y - 1) % 7])

elif x==7:
    print(day[(31+28+31+30+31+30 + y - 1) % 7])

elif x==8:
    print(day[(31+28+31+30+31+30+31 + y - 1) % 7])

elif x==9:
    print(day[(31+28+31+30+31+30+31+31 + y - 1) % 7])

elif x==10:
    print(day[(31+28+31+30+31+30+31+31+30 + y - 1) % 7])

elif x==11:
    print(day[(31+28+31+30+31+30+31+31+30+31 + y - 1) % 7])

elif x==12:
    print(day[(31+28+31+30+31+30+31+31+30+31+30 + y - 1) % 7])
