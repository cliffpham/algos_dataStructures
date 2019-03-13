import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            lis([3,1,3,2,4,1,7,8]),
            5
        ),
    def test2(self):
        self.assertEqual(
            lis([3,4,-1,0,6,2,3]),
            4
        ),
    def test3(self):
        self.assertEqual(
            lis([2,2]),
            1
        )
def rec(arr, i, last_selected_index, cache):
    ck = "%s:%s" % (i, last_selected_index)

    if ck in cache:
        return cache[ck]

    if i >= len(arr):
        return 0

    l = rec(arr, i+1, last_selected_index,  cache)
    
    r = 0
    if last_selected_index is None or last_selected_index < arr[i]:
        r = rec(arr, i+1, arr[i], cache) + 1

    cache[ck] = max(l,r)
 
    return max(l,r)

def lis(arr):
 
    return rec(arr, 0, None, {})

if __name__ == "__main__":
    unittest.main()


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
