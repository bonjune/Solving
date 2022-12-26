max_r = -10000
max_i = 0

for i in range(3):
    p, w = map(int, input().split())

    price = p * 10
    price = price - 500 if price >= 5000 else price
    weight = w * 10
    r = weight / price
    if r > max_r :
        max_r, max_i = r, i

names = ['S', 'N', 'U']

print(names[max_i])
