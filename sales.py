# https://www.acmicpc.net/problem/8912

num_tests = int(input())

for _ in range(num_tests):
    n = int(input())
    l = list(map(int, input().split()))
    total = 0
    for i, sales in enumerate(l):
        for prev_sales in l[:i]:
            total += 1 if prev_sales <= sales else 0
    print(total)
