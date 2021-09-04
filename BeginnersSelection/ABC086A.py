def sep_input():
    line = input()
    line = line.rstrip().split(' ')
    line = [int(x) for x in line]
    return line[0], line[1]

a, b = sep_input()
if (a * b) % 2:
    print("Odd")
else:
    print("Even")
