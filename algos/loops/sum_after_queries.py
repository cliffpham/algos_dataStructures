import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]),
            [8,6,2,4]
        )

def sumEvenAfterQueries(A, queries):
    S = sum(x for x in A if x % 2 == 0)
    result = []

    for query in queries:
        x = query[0]
        k = query[1]
        
        if A[k] % 2 == 0: S -= A[k]
        A[k] += x
        if A[k] % 2 == 0: S += A[k]

        result.append(S)
                
    return result

if __name__ == "__main__":
    unittest.main()