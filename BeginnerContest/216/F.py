# Title: Max Sum Counting
# Point: Dynamic Programming(DP法:動的計画法)

def sep_input():
    n = int(input())
    a_i = input().rstrip().split(' ')
    b_i = input().rstrip().split(' ')
    a_i = [int(x) for x in a_i]
    b_i = [int(x) for x in b_i]
    return n, a_i, b_i

DIV = 998244353
N, a_i, b_i = sep_input()
print("N:", N)
print("a_i:", a_i)
print("b_i:", b_i)

a_i.sort()
b_i.sort()
print("a_i:", a_i)
print("b_i:", b_i)
