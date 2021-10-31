from decimal import Decimal, ROUND_HALF_UP
from collections import Counter, deque

def test(variable_name, x):
    print('{}: {}'.format(variable_name, x))

def node_dump(nodes):
    for node in nodes:
        print("node.index:", node.index)
        print("node.nears:", node.nears)
        print("node.sign:", node.sign)

class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = False

def main():
    n, m = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(m)]

    nodes = []
    for i in range(n + 1):
        nodes.append(Node(i))

    for i in a_b:
        a, b = i
        nodes[a].nears.append(b)
    
    # node_dump(nodes)

    ans = 0
    for i in range(1, n + 1):
        queue = deque()
        queue.append(nodes[i])
        ans += 1
        nodes[i].sign = True
        while queue:
            node = queue.popleft()
            nears = node.nears
            for near in nears:
                if nodes[near].sign == False:
                    queue.append(nodes[near])
                    ans += 1
                    nodes[near].sign = True
        for i in range(n + 1):
            nodes[i].sign = False
    print(ans)

if __name__ == '__main__':
    main()
