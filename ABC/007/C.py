def generate_linkedList(input_map):
    R = len(input_map)      # マップの行数
    C = len(input_map[0])   # マップの列数
    cnt = 0
    linkedlist = []
    for row in range(1, R-1):
        for col in range(1, C-1):
            print(f'row={row}')
            print(f'col={col}')
            print(f'cnt={cnt}\n')
            # print(input_map[row][col])
            link = []
            if input_map[row][col] == '#':
                linkedlist.append(link)
                continue
            if input_map[row][col - 1] == '.':
                link.append(cnt - 1)
            if input_map[row][col + 1] == '.':
                link.append(cnt + 1)
            if input_map[row - 1][col] == '.':
                link.append(cnt - C-2)
            if input_map[row + 1][col] == '.':
                link.append(cnt + C-2)
            cnt += 1
            linkedlist.append(link)
    return linkedlist

def main():
    R, C = map(int, input().split())
    start_y, start_x = map(int, input().split())
    goal_y, goal_x = map(int, input().split())
    input_map = [list(input()) for _ in range(R)]

    flag = (R - 2) * (C - 2) * [False]      # 訪れたことがあるかどうかのフラグ
    print(flag)
    print(len(flag))

    print(f'R={len(input_map)}, C={len(input_map[0])}')
    print(*input_map, sep='\n')

    linkedlist = generate_linkedList(input_map)
    print(linkedlist)

if __name__ == '__main__':
    main()
