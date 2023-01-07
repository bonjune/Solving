# https://www.acmicpc.net/problem/25305
# 커트라인

N, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

p = nums[0]
i = 1
j = len(nums) - 1

while i < j:
    if nums[i] < p:
        nums[i], nums[0] = nums[0], nums[i]
    i += 1
    if nums[j] > nums[p]


