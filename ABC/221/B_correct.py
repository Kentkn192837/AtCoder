"""
プログラム作成ユーザー: https://atcoder.jp/contests/abc221/submissions/26316494
"""

s = input()
t = input()
 
if s == t:
    print("Yes")
    exit()
 
f = False
for i in range(len(s)):
    if s[i]==t[i]:
        continue
    if i == len(s)-1:
        print("No")
        exit()
    if s[i+1]==t[i] and s[i]==t[i+1]:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
