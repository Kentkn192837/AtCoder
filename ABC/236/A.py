def main():
    S = list(input())
    a, b = map(int, input().split())

    a -= 1
    b -= 1
    ch_a = S[a]
    ch_b = S[b]

    S[a] = ch_b
    S[b] = ch_a
    print(''.join(S))

if __name__ == '__main__':
    main()
