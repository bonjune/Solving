# https://www.acmicpc.net/problem/15649
# N과 M

N, M = list(map(int, input().split()))

nums = list(range(1, N + 1))
s = []

def nprint(ns):
    for n in ns:
        print(n, end=' ')
    print()

def solve(ns: list[int], s: list[int], m):
    if m == 0:
        nprint(s)
        return
    
    for i, n in enumerate(ns):
        solve(ns[:i] + ns[i+1:], s + [n], m - 1)

solve(nums, [], M)