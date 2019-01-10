def rec_lis(seq, cache={}): 
    def L(cur): 
        if cur in cache:
            cache[cur]
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre)) 
                cache[cur] = res
        return res
    return max(L(i) for i in range(len(seq)))

print(rec_lis([3,4,-1,0,6,2,3]))
print(rec_lis([3,1,3,2,4,1,7,8]))

# def iter_lis(arr):
#     LIS = [1 for _ in range(len(arr))]
#     print(LIS)
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[j] < arr[i]:
#                 LIS[i] = max(LIS[i], LIS[j] + 1)
#                 print(LIS)
#     return max(LIS)


# # print(iter_lis([3,1,3,2,4,1,7,8]))
# print(iter_lis([3,4,-1,0,6,2,3]))