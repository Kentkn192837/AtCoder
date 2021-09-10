def sep_input():
    n = int(input())
    line = input().rstrip().split(' ')
    return n, [int(x) for x in line]

def search(n, p):
    q = [''] * n
    for i, val in enumerate(p):
        q[val - 1] = i + 1
    q = [str(x) for x in q]
    return ' '.join(q)

N, P = sep_input()
Q = search(N, P)
print(Q)
