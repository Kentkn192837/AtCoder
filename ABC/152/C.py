from copy import deepcopy

def main():
    n = int(input())
    p = list(map(int, input().split()))

    comp_p = sorted(deepcopy(p))
    i_count = 0
    for i in comp_p:
        satisfy = []
        p_i = p.index(i)
        for j in range(p_i, -1, -1):
            if i <= p[j]:
                satisfy.append(True)
            else:
                satisfy.append(False)
        if False not in satisfy:
            i_count += 1
    print(i_count)

if __name__ == '__main__':
    main()
