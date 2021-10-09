import bisect

n, p = map(int,input().split())
score_list = list(map(int, input().split()))

score_list = sorted(score_list)
print(bisect.bisect_left(score_list, p))
