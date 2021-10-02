"""
不正解 AC×11 WA×4
"""

s = list(input())
t = list(input())
incorrect_count = 0
 
for i, j in zip(s, t):
    if i != j:
        incorrect_count += 1
 
print("No") if incorrect_count >= 3 else print("Yes")
