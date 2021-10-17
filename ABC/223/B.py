def shift(s):
    strings = []
    for _ in range(len(s)):
        last = s.pop(0)
        s.append(last)
        strings.append(''.join(s))
    return strings

s = list(input())
shifted_list = shift(s)
print(min(shifted_list))
print(max(shifted_list))
