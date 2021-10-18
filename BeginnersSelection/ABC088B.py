def game(a):
    alice = []
    bob = []
    i = 0
    while a:
        if i % 2:
            bob.append(max(a))
        else:
            alice.append(max(a))
        a.remove(max(a))
        i += 1
    return sum(alice) - sum(bob)

n = int(input())
a = list(map(int, input().split()))
ans = game(a)
print(ans)
