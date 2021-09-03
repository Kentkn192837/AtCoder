class ManyBalls():
    log = ''

    def __init__(self, n):
        self.calc(n)

    def calc(self, n):
        while n >= 1:
            if n % 2 == 1:
                self.magic_A()
                n -= 1
            else:
                self.magic_B()
                n /= 2
                n = int(n)

    def magic_A(self):
        self.log += 'A'

    def magic_B(self):
        self.log += 'B'

N = int(input())
result = ManyBalls(N)
print(result.log[::-1])
