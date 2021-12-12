def main():
    s = input()
    n = len(s)

    ans = [0] * n
    cnt = 0
    # RLとなっているようなRについて、左側に連続するRの数を数えていく
    for i, val in enumerate(s):
        if val == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    
    # 反転させて今度はRLとなっているようなLについて、右側に連続するLの数を数える
    ans = ans[::-1]
    cnt = 0
    for i, val in enumerate(s[::-1]):
        if val == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    print(*ans[::-1], sep=' ')

if __name__ == '__main__':
    main()
