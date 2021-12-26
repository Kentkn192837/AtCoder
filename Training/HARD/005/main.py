# ヒープキューアルゴリズムの利用
import heapq

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    # 最大値を取り出すために商品の価格に-1を掛ける
    a = [x * -1 for x in a]

    # リストを優先度付きキューに変換
    heapq.heapify(a)

    for _ in range(m):
        # 割引したい商品の価格を取り出す
        tmp = heapq.heappop(a)

        # 負の値を正にする
        tmp *= -1

        # 割引
        tmp //= 2
        
        # 負の値に戻す
        tmp *= -1

        # ヒープキューに戻す
        heapq.heappush(a, tmp)

    ans = -sum(a)
    print(ans)

if __name__ == '__main__':
    main()
