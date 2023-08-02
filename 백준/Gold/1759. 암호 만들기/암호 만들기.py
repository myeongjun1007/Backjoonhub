import sys
sys.setrecursionlimit(100000)

vowels = list("aeiou")
consonants = list("bcdfghjklmnopqrstvwxyz")


L , C = map(int, sys.stdin.readline().split())

alphabet_list = list(sys.stdin.readline().split())
alphabet_list.sort()
vowel_cnt = 0
consonant_cnt = 0
code_list=[0 for _ in range(L)]

def code(depth,start_idx, target_list):

    global L
    global vowel_cnt, consonant_cnt
    global code_list
    global vowels , consonants

    if depth == L:
        if (vowel_cnt >= 1) and (consonant_cnt >= 2):
            code_list.sort()
            for char in code_list:
                print(char,end='')
            print()


            return

        return
    for idx in range(start_idx,len(target_list)):
        code_list[depth] = target_list[idx]
        if code_list[depth] in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
        # print(f"depth : {depth}, vowel_cnt:{vowel_cnt}, consonant_cnt : {consonant_cnt}")
        # print(code_list)

        code(depth+1, idx+1, target_list)
        if code_list[depth] in  vowels:
            vowel_cnt -= 1
        else :
            consonant_cnt -= 1


code(0,0,alphabet_list)
