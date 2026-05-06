from itertools import combinations
from math import floor
target = list(map(int, input().split()))
N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]

for r in range(1, N+1):
    for subset in combinations(range(N), r):
        selected_colors = [colors[i] for i in subset]
        # print(selected_colors)
        # print("len: ", len(selected_colors))
        a = 0
        b = 0
        c = 0
        for idx in range(len(selected_colors)):
            # print("idx: ", idx)
            a += selected_colors[idx][0]
            b += selected_colors[idx][1]
            c += selected_colors[idx][2]
        a = floor(a / len(selected_colors))
        b = floor(b / len(selected_colors))
        c = floor(c / len(selected_colors))
        if a == target[0] and b == target[1] and c == target[2]:
            print("Yes")
            exit()
        # print("a: ", a)
        # print("b: ", b)
        # print("c: ", c)
        # print("-------")
print("No")
