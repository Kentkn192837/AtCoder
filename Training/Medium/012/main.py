def show(A):
    for a in A:
        print(''.join(a))

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    print(a)

    row = []
    col = []
    
    # 横のチェック
    a = [x for x in a if '#' in x]
    print(a)

    # 縦のチェック
    for i in range(len(a[0])):
        for j in range(len(a)):
            



if __name__ == '__main__':
    main()
