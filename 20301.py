from collections import deque

N, K, M = map(int, input().split())

m = 0
dir = True
queue = deque(range(1, N+1))

while len(queue):
    if dir:
        for _ in range(K-1):
            queue.append(queue.popleft())
    else:
        for _ in range(K):
            queue.appendleft(queue.pop())
    
    print(queue.popleft())
    m += 1
    if m % M == 0:
        dir = not dir