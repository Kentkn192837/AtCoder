"""
問題AtCoderRegularContest031: https://atcoder.jp/contests/arc031/tasks/arc031_2
プログラム実装例引用元ページ: https://qiita.com/keisuke-ota/items/6c1b4846b82f548b5dec
"""

from collections import deque

class Node:
    def __init__(self,row,col):
        self.col = col
        self.row = row
        self.nears = [[row,col-1],[row,col+1],[row-1,col],[row+1,col]]
        self.sign = False

    def __repr__(self):
        return f'Node row:{self.row} Node col:{self.col} nears:{self.nears} sign:{self.sign}'

# 入力の読み込み
h = 10
w = 10
pic = []
for i in range(h):
    pic.append(list(input()))

# 10 x 10 のインスタンス（Node）を生成し、nodes に格納する。
nodes = []
# 陸地面積を maru とする
maru = 0
for i in range(h): 
    nodes.append([])
    for j in range(w):
        nodes[i].append(Node(i,j)) 
        # 陸地をカウントする
        if pic[i][j] == "o":
            maru += 1

# 10 x 10 のマス目について海かどうかを判定し
# 海であれば一マスずつ埋め立てて陸続きかどうかを BFS(幅優先探索) で調べる。
for i in range(h):
    for j in range(w):

        # 探索候補を deque に入力する
        queue = deque()

        # 海のマス目を起点に BFS(幅優先探索) を実施する。
        if pic[i][j] == "x":
            queue.append(nodes[i][j])
            nodes[i][j].sign = True

        # 陸続きの面積を cnt とする
        cnt = 0

        # queue がなくなるまで DFS(深さ優先探索) を続ける
        while queue:
            # queue の末尾から探索候補をひとつ取り出す
            node = queue.pop()
            # 取り出した探索候補の隣接 node を取得する
            nears = node.nears
            for near in nears:
                # 探索範囲が 10 x 10 の中であることを確認する
                if 0 <= near[0] and near[0] < h and 0 <= near[1] and near[1] < w:
                    # 探索候補が訪れたことがあるかどうかを確認する
                    if nodes[near[0]][near[1]].sign == False:
                        # 訪れていなければ、海か陸かを調べる
                        # 陸であれば訪れたことにして queue に追加する。
                        if pic[near[0]][near[1]]=='o':
                            cnt += 1 
                            nodes[near[0]][near[1]].sign = True
                            queue.append(nodes[near[0]][near[1]])

        # 陸続き面積が陸地面積と等しければ、全陸地が繋がっているといえる。探索を終える
        if cnt == maru:
            print('YES')
            exit()

        # 探索済みの陸地をすべて未探索に初期化する
        for a in range(h):
            for b in range(w):
                nodes[a][b].sign = False

# どこを埋め立てても陸続きにならなかった場合は No を出力する
print('NO')
