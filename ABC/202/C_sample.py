"""
解答例:https://atcoder.jp/contests/abc202/submissions/26853748
"""

import sys
import math,itertools,bisect,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(10**8)
 
#入力
input = sys.stdin.readline
inp = lambda : int(input())
inpl = lambda : list(map(int,input().split()))
inpl_1 = lambda : list(map(lambda x:int(x)-1, input().split()))
inpl_s = lambda : list(input().split())
inpl_grid = lambda H: [input() for i in range(H)]
inpl_2d = lambda H: [list(map(int,input().split())) for i in range(H)]
 
#各種定数
INF = float("INF")
MOD = 10**9+7 #問題によって変える
 
#各種関数
def stoi(ch,zero = "a"):
    return ord(ch)-ord(zero)
 
def itos(num,zero = "a"):
    return chr(num+ord(zero))
 
def yes_no(cond, Yes = "Yes", No = "No"):
    if cond:
        print(Yes)
    else:
        print(No)
N = inp()
A = inpl()
cnt = [0]*(N+1)
for i in A:
    cnt[i] += 1
B = inpl()
C = inpl_1()
ans = 0
for i in range(N):
    ans +=cnt[B[C[i]]]
print(ans)
