from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    order = sys.stdin.readline().split()
    ftn = order[0]

    if ftn == 'push':
        num = int(order[1])
        queue.append(num)

    elif ftn == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif ftn == 'size':
        print(len(queue))

    elif ftn == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif ftn == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

    elif ftn == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
