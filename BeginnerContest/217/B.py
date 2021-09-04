def sep_input():
    given_list = []
    for _ in range(3):
        line = input()
        given_list.append(line)
    return given_list

given_list = sep_input()
comp = ['ABC', 'ARC', 'AGC' , 'AHC']

for val in given_list:
    comp.remove(val)
print(comp[0])
