from itertools import pairwise

gears = [input() for _ in range(4)]

K = int(input())
rotations = []
for _ in range(K):
    rotations.append(map(int, input().split()))

def rotate_clk(gear):
    return gear[-1] + gear[:7]


def rotate_cntr_clk(gear):
    return gear[1:] + gear[0]


def point(gears):
    total = 0
    for i, g in enumerate(gears):
        if g[0] == '1':
            total += (2 ** i)
    return total

def rotate(i, clk):
    global gears

    conns = [p[0][2] != p[1][-2] for p in pairwise(gears)]
    _clk = -clk

    if clk == 1:
        gears[i] = rotate_clk(gears[i])
    else:
        gears[i] = rotate_cntr_clk(gears[i])
    
    clk = -clk

    for j in range(i+1, 4):
        if not conns[j-1]: break
        if clk == 1: gears[j] = rotate_clk(gears[j])
        else: gears[j] = rotate_cntr_clk(gears[j])
        clk = -clk
    
    for j in range(i-1, -1, -1):
        if not conns[j]: break
        if _clk == 1: gears[j] = rotate_clk(gears[j])
        else: gears[j] = rotate_cntr_clk(gears[j])
        _clk = -_clk


for i, c in rotations:
    rotate(i-1, c)

print(point(gears))