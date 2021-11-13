from itertools import permutations

def main():
    s = input()
    ans = 1
    cand = sorted(list(permutations(s)))
    for i in range(1, len(cand)):
        if cand[i-1] != cand[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
