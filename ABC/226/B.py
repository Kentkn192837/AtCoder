from collections import deque

def main():
    n = int(input())

    cand = deque()
    ans = 1
    for i in range(n):
        seq = deque(map(int, input().split()))
        l = seq.popleft()
        cand.append(seq)

    cand = sorted(cand)

    for i in range(1, n):
        if cand[i-1] != cand[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
