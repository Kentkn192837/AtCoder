def sep_input():
    n = int(input())
    a_i = input().rstrip().split(' ')
    b_i = input().rstrip().split(' ')
    a_i = [int(x) for x in a_i]
    b_i = [int(x) for x in b_i]
    return n, a_i, b_i

DIV = 998244353
N, a_i, b_i = sep_input()
