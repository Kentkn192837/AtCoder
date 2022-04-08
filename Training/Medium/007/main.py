def main():
    N = int(input())
    S = input()

    max_cand = 0
    
    for i in range(1, len(S) - 1):
        left = list(S[:i])
        right = list(S[i:-1])
        matched_list = list(set(left) & set(right))
        max_cand = max(max_cand, len(matched_list))
    
    print(max_cand)

if __name__ == '__main__':
    main()
