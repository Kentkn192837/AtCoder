s = input()
t = input()

if s == t:
    print("Yes")
    exit()
else:
    for i in range(len(s) - 1):
        u = list(s)
        u[i], u[i+1] = u[i+1], u[i]
        u = ''.join(u)
        if u == t:
            print("Yes")
            exit()
print("No")
