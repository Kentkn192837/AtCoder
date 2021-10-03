"""
尺取り法(差分計算)
"""
from collections import Counter

n, k = map(int, input().split())
c = list(map(int, input().split()))
counter = Counter(c[0:k])
max = len(counter)
for i in range(1, n - k + 1):
    counter[c[i-1]] -= 1
    counter[c[i+k-1]] += 1
    if counter[c[i-1]] == 0:
        del counter[c[i-1]]
    max = len(counter) if max <= len(counter) else max
    if max == k:
        break
print(max)
