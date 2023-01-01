# 연속합 (Dynamic Programming)
# https://www.acmicpc.net/problem/1912

N = int(input())
nums = list(map(int, input().split()))

ans = nums[0]
dp = [nums[0]] * N

for i, n in enumerate(nums[1:]):
    dp[i+1] = n if dp[i] < 0 else dp[i] + n
    ans = max(ans, dp[i+1])

print(ans)
