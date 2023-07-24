import sys
from collections import deque

N = int(sys.stdin.readline())

# def card(n):
deck = deque([i for i in range(1,N+1)])

cnt = 0
while len(deck) > 1:
    cnt += 1
    deck.popleft()
    if len(deck) == 1:
        break
    deck.rotate(-1)
    # print(f"cnt:{cnt}")
    # print(f"deck:{deck}")

print(*deck)