"""
問題の番号を1,2,3,...の順にやっているとはいっていないというパターン
参考解答例:https://atcoder.jp/contests/abc151/submissions/26694059
"""
            
def main():
    N, M = map(int, input().split())
 
    ac = {}
    wa = {}
    for _ in range(M):
        p, s = input().split()
        if s == 'AC':
            if p not in ac:
                ac[p] = 1
        else:
            if p not in ac:
                if p not in wa:
                    wa[p] = 0
                wa[p] += 1

    cnt_ac = 0
    cnt_wa = 0
    for ack in ac.keys():
        cnt_ac += ac[ack]
        if ack in wa:
            cnt_wa += wa[ack]
    
    print(cnt_ac, cnt_wa)

if __name__ == '__main__':
    main()
