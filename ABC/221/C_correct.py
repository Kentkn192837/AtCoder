"""
プログラム作成ユーザー: https://atcoder.jp/contests/abc221/submissions/26321407
"""

def main():
    import sys
    from builtins import int
    def input(): return sys.stdin.readline().rstrip()
 
    N = sorted(input(), reverse=True)
    # N = sorted(input())[::-1]
    A = N[0::2]     # 偶数
    B = N[1::2]     # 奇数
 
    for i in range(min(len(A), len(B))):
        if A[i] != B[i]:
            A[i], B[i] = B[i], A[i]
            break
 
    print(int("".join(A)) * int("".join(B)))
 
 
main()
