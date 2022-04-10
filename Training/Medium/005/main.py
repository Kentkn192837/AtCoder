def calc(n):
    return n * (n + 1) // 2

def main():
    N = int(input())
    print(calc(N - 1))
    
if __name__ == '__main__':
    main()
