N, K, M = map(int, input().split())

class Josephus:
    def __init__(self) -> None:
        self.people = list(range(1, N+1))
        self.cnt = 0
        self.i = 0
        self.dir = 1
    
    def start(self):
        global N
        while self.cnt < N:
            self._next()
    
    def _next(self):
        global N, K, M

        i, j = 0, 0
        while abs(i) < K:
            if self.people[(self.i + j) % N] is None:
                j += self.dir
                continue
            j += self.dir
            i += self.dir
        self.i = (self.i + j - self.dir) % N
        print(self.people[self.i])
        self.people[self.i] = None
        self.cnt += 1
        self.dir = self.dir if self.cnt % M else -self.dir

        

j = Josephus()
j.start()
