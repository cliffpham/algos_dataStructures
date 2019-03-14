import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([0,1,0,3,12]),
            [1,3,12,0,0]
        ),
    def test2(self):
        self.assertEqual(
            solve([0,0,1,3,12]),
            [1,3,12,0,0]
        )
    
#O(n) faster solution
def solve(arr):
    length = len(arr)
    i = 0
    while i < length:
        if arr[i] == 0:
            del arr[i]
            arr.append(0)
            length -= 1
        else:
            i += 1

    return arr

if __name__ == "__main__":
    unittest.main()

#O(n)^2 intial solution

# def switch(arr, i):
#     temp = arr[i]
#     arr[i] = arr[i+1]
#     arr[i+1] = temp

# def solve(arr):
#     for r in range(len(arr)-1, -1, -1):
#         if arr[r] == 0:
#             for i in range(r, len(arr)-1):
#                 switch(arr, i)

#     return arr

