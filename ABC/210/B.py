def judge(n, s):
    for i, val in enumerate(list(s)):
        if int(val) == 1:
            return 'Takahashi' if i % 2 == 0 else 'Aoki'

n = int(input())
s = input()
result = judge(n, s)
print(result)
