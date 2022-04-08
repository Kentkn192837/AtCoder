def main():
    N = int(input())
    S = input()

    max_cand = 0
    
    for i in range(1, N):
        matched_list = set(S[:i]) & set(S[i:])
        max_cand = len(matched_list) if max_cand < len(matched_list) else max_cand
    print(max_cand)

if __name__ == '__main__':
    main()
