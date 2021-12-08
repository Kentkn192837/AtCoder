def main():
    s = input()
    b_cnt = 0
    ans = 0
    # 文字列の先頭からBの数を数えて、もしi番目の文字がWならそこまでにあったBの数をansに足す
    for i in s:
        if i == 'W':
            ans += b_cnt
        else:
            b_cnt += 1
    print(ans)

if __name__ == '__main__':
    main()
