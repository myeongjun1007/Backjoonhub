resistor_value = dict(black =0, brown=1, red=2, orange=3, yellow=4, green=5, blue=6, violet=7, grey=8 ,white=9)
resistor_mul = dict(black =1, brown=10**1, red=10**2, orange=10**3, yellow=10**4, green=10**5, blue=10**6, violet=10**7, grey=10**8 ,white=10**9)

first_color = ""
second_color = ""
third_color = ""

for i in range(3):
    now_color = input()
    if i==0:
        for j in resistor_value:
            if j== now_color:
                first_color= j

    elif i==1:
        for j in resistor_value:
            if j== now_color:
                second_color= j

    else:
        for j in resistor_value:
            if j == now_color:
                third_color = j

result = (resistor_value[first_color] * 10 + resistor_value[second_color]) * resistor_mul[third_color]
print(result)