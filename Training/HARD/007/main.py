import heapq

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c_b = []
    for _ in range(m):
        b, c = map(int, input().split())
        c_b.append([c, b])
    c_b = sorted(c_b, reverse=True)

    heapq.heapify(a)

    for i in range(m):
        c, b = c_b[i]
        for j in range(b):
            tmp = heapq.heappop(a)
            if tmp < c:
                heapq.heappush(a, c)
            else:
                heapq.heappush(a, tmp)
                break
    ans = sum(a)
    print(ans)

if __name__ == '__main__':
    main()
