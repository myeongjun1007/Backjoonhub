# 10828 스택
import sys
N = int(sys.stdin.readline())
stack = []


def push(num):
    stack.append(num)

def pop():

    if len(stack) == 0:
        print(-1)

    else:
        print(stack.pop())
        

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)

    else:
        print(stack[-1])


for i in range(1,N+1):
    operation = list(sys.stdin.readline().split())
    method = operation[0]

    if method == 'push':
        num = int(operation[1])

        push(num)

    elif method == 'pop':
        pop()

    elif method == 'size':
        size()

    elif method =='empty':
        empty()

    elif method == 'top':
        top()