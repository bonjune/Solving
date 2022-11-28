# https://www.acmicpc.net/problem/1064

def slope(x, y):
    if x[1] == y[1]:
        return None
    return (x[0] - y[0]) / (x[1] - y[1])

def impossible(x, y, z):
    s1 = slope(x, y)
    s2 = slope(y, z)
    if s2 is None:
        return True
    if s1 == s2:
        return True
    return False

def dist(x, y):
    d1 = abs(x[0] - y[0])
    d2 = abs(x[1] - y[1])
    return (d1 ** 2 + d2 ** 2) ** 0.5


def main():
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))

    A = (x1, y1)
    B = (x2, y2)
    C = (x3, y3)

    if impossible(A, B, C):
        print(-1)
        return
    
    d1 = dist(A, B) + dist(B, C)
    d2 = dist(A, C) + dist(C, B)
    d3 = dist(A, B) + dist(C, A)
    
    max_d = max(d1, d2, d3)
    min_d = min(d1, d2, d3)

    print(f"{(max_d - min_d) * 2:.10f}", )

main()
