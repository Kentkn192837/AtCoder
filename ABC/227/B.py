def test(variable, x):
    print('{}: {}'.format(variable, x))

def main():
    # n = int(input())
    # s = list(map(int, input().split()))
    calc_result = []
    for b in range(1, 17):
        for a in range(b, 17):
            mul = 4 * a * b + 3 * a + 3 * b
            if mul <= 1000:
                calc_result.append(mul)
    calc_result.sort()
    ans = 0
    # for i in s:
    #     if i not in calc_result:
    #         ans += 1
    print(calc_result)

if __name__ == '__main__':
    main()
