def sep_input():
    line = input()
    line = line.rstrip().split(' ')
    line = [int(x) for x in line]
    return line[0], line[1]

a = int(input())
b, c = sep_input()
str = input()

sum = a + b + c

print(sum, str)
