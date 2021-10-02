from math import floor

def zfill(x):
    return str(floor(x)).zfill(2)

def calc(m):
    if m < 0.1:
        return '00'
    elif 0.1 <= m and m <= 5:
        return zfill(m * 10)
    elif 6 <= m and m <= 30:
        return zfill(m + 50)
    elif 35 <= m and m <= 70:
        return zfill((m - 30) / 5) + 80)
    elif 70 <= m:
        return 89

m = int(input()) / 1000
vv = calc(m)
print(vv)
