"""
尺取り法(差分計算)
"""

n, k = map(int, input().split())
c = list(map(int, input().split()))
max = 0
for i in range(n - k + 1):
    comp = []
    for j in c[i:i + k]:
        if j not in comp:
            comp.append(j)
    if max <= len(comp):
        max = len(comp)
    if max == k:
        break
print(max)
