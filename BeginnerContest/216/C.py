class ManyBalls():
    log = ''

    def __init__(self, n):
        self.init_n = n
        self.calc(n)

    def calc(self, n):

        while True:
            if n == 1:
                return

            if n % 2 == 1:
                self.magic_A()
                n -= 1
                continue

            if n % 2 == 0:
                self.magic_B()
                n /= 2
                n = int(n)
                continue

    def magic_A(self):
        self.log += 'A'

    def magic_B(self):
        self.log += 'B'

N = int(input())
result = ManyBalls(N)
print('A{}'.format(result.log[::-1]))
