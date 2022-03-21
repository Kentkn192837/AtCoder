import bisect

def main():
    N = int(input())
    numbers = [x + 1 for x in range(2 * N + 1)]
    
    T = numbers.pop()
    print(T)

    while True:
        A = int(input())
        if A == 0: break
        numbers.pop(bisect.bisect_left(numbers, A))
        T = numbers.pop()
        print(T)

if __name__ == '__main__':
    main()
