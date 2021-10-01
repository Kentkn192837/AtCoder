"""
問題URL:https://atcoder.jp/contests/dp/tasks/dp_a
"""

def DP_search(h):
    nodes = [0]
    nodes.append(abs(h[1] - h[0]))
    for i in range(2, len(h)):
        a = abs(h[i] - h[i-1]) + nodes[i-1]
        b = abs(h[i] - h[i-2]) + nodes[i-2]
        nodes.append(a if a < b else b)
    return nodes

def main():
    n = int(input())
    h = list(map(int, input().split()))
    nodes = DP_search(h)
    print(nodes[n-1])

if __name__ == '__main__':
    main()
