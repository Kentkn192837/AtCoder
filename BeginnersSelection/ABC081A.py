s_list = list(input())
s_list = [int(x) for x in s_list]
score = 0

for val in s_list:
    if val:
        score += 1

print(score)
