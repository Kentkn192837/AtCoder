def generate(str_list, t):
    str = ''
    for i in t:
        str += str_list[i - 1]
    return str

str_list = [input() for _ in range(3)]
t = list(map(int, list(input())))
result = generate(str_list, t)
print(result)
