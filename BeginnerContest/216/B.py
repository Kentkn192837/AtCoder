import copy

def sep_input():
    name_list = []
    line = input().rstrip()
    n = int(line)
    for _ in range(n):
        line = input().rstrip()
        name_list.append(line)
    return n, name_list

def check(name_list):
    comp_list = copy.deepcopy(name_list)
    for i, name in enumerate(name_list):
        comp_list.pop(0)
        if len(comp_list) == 0:
            return "No"
        if name in comp_list:
            return "Yes"
    return "No"

N, name_list = sep_input()
result = check(name_list)
print(result)
