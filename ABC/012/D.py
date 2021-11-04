"""
ソースコード実装例:https://nashidos.hatenablog.com/entry/2020/04/07/100508
"""
import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq)
    cost = [float('inf')] * n
    cost[s] = 0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]:
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

def main():
    n, m = map(int, input().split())
    e = [[] for _ in range(n)]

    for _ in range(m):
        a, b, t = map(int, input().split())
        a, b = a-1, b-1
        e[a].append((t, b))
        e[b].append((t, a))
    
    ans = float('inf')

    for i in range(n):
        dist = dijkstra(i)
        ans = min(ans, max(dist))
    print(ans)

if __name__ == '__main__':
    main()
