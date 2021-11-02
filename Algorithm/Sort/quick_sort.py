def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr
    
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [arr] * ref_count + right

"""
・基準値を決めて、その基準値から見て大小の2つの配列に分ける。
・この基準値の選び方として、配列の最初や最後、適当な3つぐらいの値の中央値などを用いる。
・分けたグループの中で、更に再帰的に同じ処理を行っていく。
・基準値の決め方に性能が左右される。
・ある程度まで分割できたら、別のソートアルゴリズムを用いることで高速化出来る。
・かなり早いがメモリを多く使う。
・安定なソートではない。
"""
