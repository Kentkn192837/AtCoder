import copy

def sep_input():
    def sep_line():
        line = input().rstrip().split(' ')
        line = [int(x) for x in line]
        return line[0], line[1]

    l, q = sep_line()
    input_list = []
    for _ in range(q):
        line = input().rstrip().split(' ')
        line = [int(x) for x in line]
        input_list.append(line)
    return l, q, input_list

def run(l, q, query):
    L = []
    for i in range(l):
        L.append(i)
    comp_L = copy.deepcopy(L)

    for i, val in enumerate(query):
        if val[0] == 1:
            L = L[val[1]:]
        else:
            a = comp_L[:val[1]]
            b = comp_L[val[1]]
            
            print("L:", len(L))

L, Q, input_list = sep_input()
run(L, Q, input_list)
