n, m = map(int, input().split())
a_seaquence = list(map(int, input().split()))
b_seaquence = list(map(int, input().split()))

a_seaquence = list(set(a_seaquence))
b_seaquence = list(set(b_seaquence))

min_candidate = []
for i in a_seaquence:
    candidate = []
    for j in b_seaquence:
        candidate.append(abs(j - i))
    min_candidate.append(min(candidate))
print(min(min_candidate))
