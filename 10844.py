# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844


N = int(input())

dp = [[0] + [1] * 9]

for _ in range(N-1):
    dp.append([0] * 10)


for i in range(1, N):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N-1]) % 1_000_000_000)