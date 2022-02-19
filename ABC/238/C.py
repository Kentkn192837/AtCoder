MOD = 998244353

def same_dig_most_min(num):
    num = str(num)
    dig = len(num)
    most_min = '1'
    most_min += '0' * (dig - 1)
    return int(most_min), dig

def calc_sum(dig):
    a = 1
    l = '9'
    l += '0' * (dig - 1)
    l = int(l)
    n = l
    amount = n * (a + l) / 2
    return int(amount)

def main():
    N = int(input())
    result = 0
    last_result = 0
    most_min, dig = same_dig_most_min(N)
    for i in range(1, dig):
        result += calc_sum(i)
    
    roop_time = N - most_min + 1
    
    for i in range(roop_time + 1):
        result += i
    print(result % MOD)

if __name__ == '__main__':
    main()
