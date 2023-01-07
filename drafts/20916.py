# https://www.acmicpc.net/problem/20916
# 안녕 2020 안녕 2021


def is_hello(a: int, b: int):
    nstr = str(a + b)
    return nstr[:4] == "2020" and nstr[-4:] == "2021"
    
a: dict[int, int] = {}


def merge(ls: list[int], rs: list[int]):
    total = 0

    for n in ls:
        for m in rs:
            if is_hello(n, m):
                total += a[n] * a[m]
    
    return total


def find_hello_pairs(ns: list[int]):
    if len(ns) == 0:
        return 0

    if len(ns) == 1:
        n = ns[0]
        return is_hello(n, n)

    ls = ns[:len(ns)//2]
    rs = ns[len(ns)//2:]

    lc = find_hello_pairs(ls)
    rc = find_hello_pairs(rs)
    mc = merge(ls, rs)

    return lc + rc + mc


def solve(nums: list[int]):
    global a
    a = {}
    for n in nums:
        if not n in a:
            a[n] = 0
        a[n] += 1

    ns = list(a.keys())
    ans = find_hello_pairs(ns)
    print(ans)

T = int(input())
nums = []

for _ in range(T):
    _ = input()
    nums.append(list(map(int, input().split())))

for i in range(T):
    solve(nums[i])
