# 등차수열의 합
# https://www.acmicpc.net/problem/1419

l = int(input())
r = int(input())
k = int(input())

def round_down(n, k):
    return n // k * k

def round_up(n, k):
    return (n // k + 1) * k if n % k else n

if k == 2:
    l = max(l, 3)
    print(max(r - l + 1, 0))

if k == 3:
    if r < 6:
        print(0)
        exit(0)
    l = max(l, 6)

    r = round_down(r, 3)
    l = round_up(l, 3)

    print((r - l) // 3 + 1)

if k == 4:
    if r < 10:
        print(0)
        exit(0)

    l = max(l, 10)

    r = round_down(r, 2)
    l = round_up(l, 2)

    print((r - l) // 2 + 1 - (l <= 12 and r >= 12))

if k == 5:
    if r < 15:
        print(0)
        exit(0)

    l = max(l, 15)

    r = round_down(r, 5)
    l = round_up(l, 5)

    print((r - l) // 5 + 1)