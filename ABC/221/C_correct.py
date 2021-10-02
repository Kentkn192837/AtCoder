"""
プログラム作成ユーザー: https://atcoder.jp/contests/abc221/submissions/26321407
入力直後のN: ['9', '9', '8', '5', '4', '4', '3', '3', '2']
A初期値: ['9', '8', '4', '3', '2']
B初期値: ['9', '5', '4', '3']
A処理後: ['9', '5', '4', '3', '2']
B処理後: ['9', '8', '4', '3']
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
