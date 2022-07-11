x = list(input())
n = int(input())
s = [input() for _ in range(n)]
largest_length = max([len(x) for x in s])
ord_list = [x for x in range(ord('z') - ord('a') + 1)]
# print(x)
# print(ord_list)
new_dict = dict(zip(x, ord_list))
for i in range(largest_length):
    
    sort_mark = []
    for j in range(len(s)):
        if 
        sort_mark.append(new_dict[s[j][i]])
    # print(s)
    # print(sort_mark)
    comp = dict(zip(s, sort_mark))
    comp = sorted(comp.items(), key=lambda x:x[1])
    s = [val[0] for _, val in enumerate(comp)]
print(comp)
