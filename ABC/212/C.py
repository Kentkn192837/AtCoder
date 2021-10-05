import bisect

n, m = map(int, input().split())
a_seaquence = list(map(int, input().split()))
b_seaquence = list(map(int, input().split()))

a_seaquence = list(set(a_seaquence))
b_seaquence = sorted(list(set(b_seaquence)))

min_candidate = []
for i in a_seaquence:
    # print('{}の処理'.format(i))
    x_index = bisect.bisect_left(b_seaquence, i)
    # print("x_index:", x_index)
    if x_index == len(b_seaquence):
        x_index -= 1
        comp = abs(i - b_seaquence[x_index])
    elif x_index == 0:
        comp = abs(i - b_seaquence[x_index])
    else:
        comp = min([abs(i - b_seaquence[x_index - 1]), abs(i - b_seaquence[x_index])])
    # print("comp", comp)
    min_candidate.append(comp)
# print("min_candidate", min_candidate)
print(min(min_candidate))
