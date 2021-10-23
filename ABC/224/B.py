from itertools import combinations

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(w)]

    h_list = list(range(h))
    w_list = list(range(w))
    print(list(combinations(h_list, 2)))
    print(list(combinations(w_list, 2)))

if __name__ == '__main__':
    main()
