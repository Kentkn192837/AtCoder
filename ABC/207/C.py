"""
2つの閉区間 [a,b],[c,d] が共通部分を持つかの判定は max(a,c)≤min(b,d) と書くことができる。
"""

def main():
    n = int(input())
    left = [0] * n
    right = [0] * n

    for i in range(n):
        t, left[i], right[i] = map(int, input().split())
        if t == 2:
            right[i] -= 0.5
        elif t == 3:
            left[i] += 0.5
        elif t == 4:
            left[i] += 0.5
            right[i] -= 0.5
    
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            ans += ( max(left[i], left[j]) <= min(right[i], right[j]) )
    print(ans)

if __name__ == '__main__':
    main()
