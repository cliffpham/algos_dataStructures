import unittest

class test(unittest.TestCase):
    def test2(self):
        self.assertEqual(
            combo([1,2,3,4,5,6,7,8,9],3,7,0,[],[]),
            [[1,2,4]]
        )

def combo (arr, k, target, i, cur, output):
    if len(cur) == k:
        if sum(cur) == target:
            output.append(cur[:])
        return

    if i == len(arr):
        return
    
    combo(arr, k, target, i+1,cur,output)

    cur.append(arr[i])
    combo(arr,k,target,i+1, cur,output)
    cur.pop()

    return output

if __name__ == "__main__":
    unittest.main()