def sep_input():
    line = input().rstrip().split(' ')
    line = [int(x) for x in line]
    return line

def get_attmpt_time(a_list):
    comp = []
    for i in a_list:
        times = 0
        while i % 2 == 0:
            i /= 2
            i = int(i)
            times += 1
        comp.append(times)    
    return min(comp)

N = int(input())
a_list = sep_input()

result = get_attmpt_time(a_list)
print(result)
