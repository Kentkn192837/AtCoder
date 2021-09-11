from copy import deepcopy

def sep_input():
    line = input().rstrip().split(' ')
    n, m = int(line[0]), int(line[1])

    que_list = []
    for i in range(2*m):
        if i % 2 == 0:
            line = input()
            continue
        line = input().rstrip().split(' ')
        line = [int(x) for x in line]
        que_list.append(line)
        
    return n, m, que_list

def search(que_list, m):
    for _ in range(m):
        comp_que = deepcopy(que_list)
        comp = []
        index = []
        for i, que in enumerate(que_list):
            if len(que) == 0:
                continue
            
            j = que[0]
            if j in comp:
                que.pop(0)
                que_list[index[comp.index(j)]].pop(0)
                index.pop(comp.index(j))
                comp.remove(j)
            else:
                comp.append(j)
                index.append(i)
        
        if comp_que == que_list:
            return False
    return True

N, M, que_list = sep_input()
flag = search(que_list, M)
if flag:
    print("Yes")
else:
    print("No")
