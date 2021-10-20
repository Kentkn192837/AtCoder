"""
今回の問題では計算量が高々4*10^4通りであることに着目して全探索できるとして考える
"""
import itertools

def search(p, q):
    p_permutations = sorted(list(map(list, itertools.permutations(p))))
    q_permutations = sorted(list(map(list, itertools.permutations(q))))
    a = p_permutations.index(p)
    b = q_permutations.index(q)
    return abs(a - b)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    ans = search(p, q)
    print(ans)

if __name__ == '__main__':
    main()
