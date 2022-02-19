def main():
    N = int(input())
    A = list(map(int, input().split()))
    record = [0]
    result = []
    rad = 360
    position = 0
    for a in A:
        position += a
        if position >= rad:
            position -= rad
        record.append(position)
    record = sorted(record)

    for i in range(-1, len(record) - 1):
        if record[i] > record[i + 1]:
            result.append(record[i + 1] + rad - record[i])
        else:
            result.append(record[i + 1] - record[i])

    print(max(result))

if __name__ == '__main__':
    main()
