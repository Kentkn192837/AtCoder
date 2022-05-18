def input_two_array(n):
    a = []
    b = []
    for _ in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    return a, b

def main():
    N, M = map(int, input().split())
    a, b = input_two_array(N)
    c, d = input_two_array(M)
    print(*a)

if __name__ == '__main__':
    main()
