from collections import Counter

def narrow_down(a, b, c):
    a = list(Counter(a).items())
    cand = Counter([b[j - 1] for j in c])
    cand_key = list(cand.keys())
    cand_val = list(cand.values())
    return a, cand_key, cand_val

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a, cand_key, cand_val = narrow_down(a, b, c)

    ans = 0
    for i in range(len(a)):
        if a[i][0] in cand_key:
            ans += 1 * a[i][1] * cand_val[cand_key.index(a[i][0])]
    print(ans)
        

if __name__ == '__main__':
    main()
