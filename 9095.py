# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

T = int(input())

def solve():
    n = int(input())
    dp = [1] + [0] * n
    
    for i in range(n):
        dp[i + 1] += dp[i]
        if i + 2 < len(dp):
            dp[i + 2] += dp[i]
        if i + 3 < len(dp):
            dp[i + 3] += dp[i]
    
    print(dp[-1])

for _ in range(T):
    solve()