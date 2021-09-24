"""
幅優先探索実装例参考ページ￥:https://qiita.com/keisuke-ota/items/6c1b4846b82f548b5dec
n: 6
m: 9
links: [[3, 4], [6, 1], [2, 4], [5, 3], [4, 6], [1, 5], [6, 2], [4, 5], [5, 6]]
node.index: [0, 1, 2, 3, 4, 5, 6]
node.sign: [-1, -1, -1, -1, -1, -1, -1]
nodes[0].nears: []
nodes[1].nears: [6, 5]
"""
from collections import deque

class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1

# n: 部屋の数 m: 通路の数 links: 通路が繋ぐ部屋
n, m = map(int, input().split())
links = [list(map(int, input().split())) for _ in range(m)]

# print("n:", n)
# print("m:", m)
# print("links:", links)

nodes = []
for i in range(n + 1):
    nodes.append(Node(i))

# print("node.index:", [node.index for node in nodes])
# print("node.sign:", [node.sign for node in nodes])

# 隣接 node を nears に格納する
for j in range(m):
    edge_start, edge_end = links[j]
    nodes[edge_start].nears.append(edge_end)
    nodes[edge_end].nears.append(edge_start) # 有向グラフの場合は消す

# print("nodes[1].nears:", nodes[1].nears)

# 空のキューを用意する
queue = deque()

# 本問では node 1 から探索を開始するため queue に node 1 を最初に入れる
queue.append(nodes[1])
while queue:
    # キューから頂点を取り出す
    node = queue.popleft()
    nears = node.nears
    
    # 隣接する頂点を調査する
    for near in nears:
        if nodes[near].sign == -1:
            # 未調査の時の処理
            queue.append(nodes[near]) # キューに未調査の頂点を追加する
            nodes[near].sign = node.index
            # print("nodes[near].sign:", nodes[near].sign)

# print("[node.sign for node in nodes]:", [node.sign for node in nodes])

# YesまたはNoを表示
if -1 in [node.sign for node in nodes][2:]:
    print('No')
    exit(0)
else:
    print('Yes')

# 道しるべを表示
for k in range(2, n + 1):
    print(nodes[k].sign)
