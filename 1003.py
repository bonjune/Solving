# https://www.acmicpc.net/problem/1003
# 피보나치 함수

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }

cache = {
    0 : (1, 0),
    1 : (0, 1)
}

def solve(n):
    if n in cache:
        return cache[n]
    
    a = solve(n - 2)
    b = solve(n - 1)
    cache[n] = (a[0] + b[0], a[1] + b[1])
    return cache[n]

T = int(input())
for _ in range(T):
    n = int(input())
    zeros, ones = solve(n)
    print(zeros, ones)


