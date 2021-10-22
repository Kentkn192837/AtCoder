def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_set = set(a)
    print('YES' if len(a) == len(a_set) else 'NO') # 出力する文字に注意Yes,No ではなく全て大文字でYES,NOで出力する

if __name__ == '__main__':
    main()
