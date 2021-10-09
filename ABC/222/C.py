def judge(a, b):
    pass

def main():
    n, m = map(int, input().split())
    attack_list = [list(input()) for _ in range(2 * n)] # じゃんけんの手
    battle_list = [[x + 1 for x in range(2 * n)]]
    win_count = [0] * 2 * n
    result_list = []

    for i in range(2 * n):
        result_list.append([battle_list[0][i], win_count[i]])
    
    for i in range(m):
        battle_list.append([0] * 2 * n)

    for i in range(m):
        for j in range(0, 2 * n, 2):
            if attack_list[result_list[j][0] - 1][i] == attack_list[result_list[j+1][0] - 1][i]:
                continue
            if attack_list[result_list[j][0] - 1][i] == 'G':
                if attack_list[result_list[j+1][0] - 1][i] == 'P':
                    result_list[j+1][1] += 1
                else:
                    result_list[j][1] += 1
            if attack_list[result_list[j][0] - 1][i] == 'C':
                if attack_list[result_list[j+1][0] - 1][i] == 'G':
                    result_list[j+1][1] += 1
                else:
                    result_list[j][1] += 1
            if attack_list[result_list[j][0] - 1][i] == 'P':
                if attack_list[result_list[j+1][0] - 1][i] == 'C':
                    result_list[j+1][1] += 1
                else:
                    result_list[j][1] += 1
        result_list = sorted(result_list)
        result_list = sorted(result_list, key=lambda x: x[-1], reverse=True)

    for i in result_list:
        print(i[0])

if __name__ == '__main__':
    main()
