from math import floor
m = int(input()) / 1000
if m < 0.1:
    vv = '00'
elif 0.1 <= m and m <= 5:
    vv = str(floor(m * 10)).zfill(2)
elif 6 <= m and m <= 30:
    vv = str(floor(m + 50)).zfill(2)
elif 35 <= m and m <= 70:
    vv = str(floor((m - 30) / 5) + 80).zfill(2)
elif 70 <= m:
    vv = 89
print(vv)
