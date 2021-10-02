"""
プログラム作成ユーザー: https://atcoder.jp/contests/abc221/submissions/26322777
"""
arr = sorted(list(map(int, list(input()))), reverse=True)
 
x,y = 0, 0
for i in arr:
    if x < y :
        x = x*10+ i
    else:
        y = y * 10 + i
 
print(x * y)
