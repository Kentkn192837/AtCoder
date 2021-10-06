import bisect

n, m = map(int, input().split())
a_sequence = list(map(int, input().split()))
b_sequence = list(map(int, input().split()))

a_sequence = list(set(a_sequence))
b_sequence = sorted(list(set(b_sequence)))

min_candidate = []
for i in a_sequence:
    # print('{}の処理'.format(i))
    x_index = bisect.bisect_left(b_sequence, i)
    # print("x_index:", x_index)
    if x_index == len(b_sequence):
        x_index -= 1
        comp = abs(i - b_sequence[x_index])
    elif x_index == 0:
        comp = abs(i - b_sequence[x_index])
    else:
        comp = min([abs(i - b_sequence[x_index - 1]), abs(i - b_sequence[x_index])])
    # print("comp", comp)
    min_candidate.append(comp)
# print("min_candidate", min_candidate)
print(min(min_candidate))
