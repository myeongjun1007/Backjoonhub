import sys
N = int(sys.stdin.readline())

def song(n):
    birds = n
    cnt = 0
    k = 1
    while birds != 0:
        if k <= birds:
            birds -= k
            cnt += 1


            #print(f"birds:{birds}, cnt:{cnt}, k:{k}")
            k += 1
        else:
            k=1
            birds -= k
            cnt += 1

            #print(f"birds:{birds}, cnt:{cnt}, k:{k}")

            k += 1

    return cnt

print(song(N))