def sep_input():
    line = input().rstrip().split(' ')
    return line[0], line[1]

s, t = sep_input()
if s < t:
    print("Yes")
else:
    print("No")
