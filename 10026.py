# https://www.acmicpc.net/problem/10026
# 적록색약

import sys
sys.setrecursionlimit(100000)

N = int(input())
grid = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def okay(y, x):
    return (0 <= y < N and 0 <= x < N) and not visited[y][x]

def cmp(c1, c2):
    return c1 == c2

def cmp_weak(c1, c2):
    if c1 == 'R' and c2 == 'G':
        return True
    if c2 == 'R' and c1 == 'G':
        return True
    return cmp(c1, c2)

def around(y, x):
    return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

def do_scan(pos: tuple[int, int], cmp):
    y, x = pos
    color = grid[y][x]
    visited[y][x] = True

    for ny, nx in around(y, x):
        if okay(ny, nx) and cmp(color, grid[ny][nx]):
            do_scan((ny, nx), cmp)

def scan(cmp):
    cnt = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                do_scan((y, x), cmp)
                cnt += 1

    return cnt

cnt_normal = scan(cmp=cmp)
visited = [[False] * N for _ in range(N)]
cnt_weak = scan(cmp=cmp_weak)

print(cnt_normal, cnt_weak)
