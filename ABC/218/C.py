def sep_input():
    n = int(input())
    s = []
    t = []
    for _ in range(n):
        line = list(input())
    
    for _ in range(n):
        line = list(input())
        t.append(line)        
    return n, s, t

def rotate(t):
    rotated = []
    for j in range(len(t[0]))[::-1]:
        low = []
        for i in range(len(t)):
            low.append(t[i][j])
        rotated.append(low)
    return rotated

def judge(s, t):
    for _ in range(4):
        if s == t:
            return "Yes"
        else:
            t = rotate(t)
    if s == t:
        return "Yes"
    return "No"

N, S, T = sep_input()
result = judge(S, T)
print(result)
