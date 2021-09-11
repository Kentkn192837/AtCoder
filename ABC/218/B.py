P = input().rstrip().split(' ')
P = [int(x) for x in P]
str = ''
for s in P:
    str += chr(s + 96)
print(str)
