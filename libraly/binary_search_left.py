def binary_search_left(sorted_list, search_value):
    """
    二分探索を実施し、検索対象の値がリスト内のどのindexに挿入可能かを返す
    一番左のindexを返す
    """
    left = 0                                 #探索する範囲の左,右端点のindex
    right = len(sorted_list) 
    while left < right:
        mid = (left + right) // 2            #探索する範囲の中央のindex
        
        if sorted_list[mid] < search_value:  #探索する値が中央の値より大きい場合、探索する範囲を右側に絞り込む
            left = mid + 1 

        else:                                #中央の値が探索する値以上の場合、mid も候補として残し、左側を探す
            right = mid
    
    return left

a=[1,2,3,3,4,4,4,5,5]
result = binary_search_left(a,4)
print(result)