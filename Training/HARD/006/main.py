NO_STRING = 'UNRESTORABLE'

def main():
    s = input()
    t = input()

    ans = []
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j] and s[i + j] != '?':
                break
        else:
            tmp = s[:i] + t
            if i + len(t) < len(s):
                tmp += s[i + len(t):]
            ans.append(tmp)
    
    if ans == []:
        print(NO_STRING)
        exit()
    
    for i in range(len(ans)):
        ans[i] = ans[i].replace('?', 'a')
    ans = sorted(ans)
    print(ans[0])

if __name__ == '__main__':
    main()
