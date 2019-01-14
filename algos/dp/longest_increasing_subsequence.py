#incomplete

def rec_lis(arr):
    """
    >>> rec_lis([3,1,3,2,4,1,7,8])
    5

    >>> rec_lis([3,4,-1,0,6,2,3])
    4

    >>> rec_lis([7,6,3,8,2,10,11,2])
    4
    """
    # set comparison to first index in list
    last_selected_index = arr[0]

    def rec(arr, last_selected_index, i, cache):
        if i in cache:
            return cache[i]

        if i >= len(arr):
            return 0

        # minimum distance to itself is 1
        l = 1 
        r = 1

        if last_selected_index <= arr[i]:
            r = rec(arr, arr[i], i+1, cache)+1

        l = rec(arr, last_selected_index, i+1, cache)
        cache[i] = max(l,r)

        return max(l,r)
        
    return rec(arr, last_selected_index,0,{})

# def rec_lis(seq, cache={}): 
#     def L(cur): 
#         if cur in cache:
#             cache[cur]
#         res = 1
#         for pre in range(cur):
#             if seq[pre] <= seq[cur]:
#                 res = max(res, 1 + L(pre)) 
#                 cache[cur] = res
#         return res
#     return max(L(i) for i in range(len(seq)))

# print(rec_lis([3,4,-1,0,6,2,3]))
# print(rec_lis([3,1,3,2,4,1,7,8]))