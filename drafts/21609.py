from pprint import pprint

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N] * N
total = 0

BLACK = -1
RAINBOW = 0

def rotate():
    global board
    new = []
    for i in range(N):
        new.append([])
        for r in board:
            new[i].append(r[i])
    new.reverse()
    board = new

def fall_block(col, row):
    global board

    for d in range(1, N-col):
        if board[col+d][row] is None:
            board[col+d][row], board[col+d-1][row] = board[col+d-1][row], board[col+d][row]

def fall():
    global board
    
    for row in range(N):
        for col in range(N-2, -1, -1):
            fall_block(col, row)

def in_board(point):
    x, y = point
    return 0 <= x < N and 0 <= y < N

def adjs(point, group):
    r = []
    x, y = point

    if in_board((x-1, y)) and (x-1, y) not in group: r.append((x-1, y))
    if in_board((x+1, y)) and (x+1, y) not in group: r.append((x+1, y))
    if in_board((x, y-1)) and (x, y-1) not in group: r.append((x, y-1))
    if in_board((x, y+1)) and (x, y+1) not in group: r.append((x, y+1))

    return r

def get_block(point):
    x, y = point
    return board[y][x]

def get_group(point, initial=None):
    b = get_block(point)
    if b is None:
        return set()
    if b == -1:
        return set()
    if initial is not None:
        if not (b == 0 or b == initial):
            return set()

    group = {point}

    for adj in adjs(point, group):
        group = group.union(get_group(adj, b))
        print(group)

    return group

def gain_from_largest_group():
    global board, total

    start = (0, 0)
    g = get_group(start)
    print(g)
    total += len(g) ** 2
    for x, y in g:
        board[y][x] = None


gain_from_largest_group()
fall()
rotate()
fall()

print(total)