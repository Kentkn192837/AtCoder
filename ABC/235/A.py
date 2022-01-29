def convert_to_int(x):
    return int(''.join(x))

def main():
    abc = list(input())
    bca = [abc[1], abc[2], abc[0]]
    cab = [abc[2], abc[0], abc[1]]
    abc = convert_to_int(abc)
    bca = convert_to_int(bca)
    cab = convert_to_int(cab)
    print(abc + bca + cab)

if __name__ == '__main__':
    main()
