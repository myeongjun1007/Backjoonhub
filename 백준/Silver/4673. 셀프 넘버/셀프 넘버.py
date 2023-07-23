def d(n):
    s_num= int(n)
    for i in list(str(n)):
        s_num += int(i)

    return s_num

s_num_list = []

for i in range(1,10000):
    s_num_list.append(d(i))

for i in range(1,10000) :
    if i not in s_num_list:
        print(i)