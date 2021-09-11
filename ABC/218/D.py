def sep_input():
    n = int(input())
    coordinate = []
    for _ in range(n):
        line = input().rstrip().split(' ')
        line = [int(x) for x in line]
        xy = (line[0], line[1])
        coordinate.append(xy)
    return n, coordinate

def judge(xy):
    

N, xy = sep_input()
result = judge(xy)
