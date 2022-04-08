def main():
    N = int(input())
    a = list(map(int, input().split()))

    rank_cnt = [0] * 8
    free_color_cnt = 0
    ans = 0

    for a_i in a:
        if a_i >= 3200:
            free_color_cnt += 1
        else:
            rank_cnt[a_i // 400] += 1

    for val in rank_cnt:
        if val > 0:
            ans += 1
    
    if ans == 0 and free_color_cnt > 0:
        print(1, free_color_cnt)
    else:
        print(ans, ans + free_color_cnt)

if __name__ == '__main__':
    main()
