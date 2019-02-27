import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            find(3, [[1,3],[2,3],[3,1]]),
            -1
        )
    def test2(self):
        self.assertEqual(
            find(2, [[2,1]]),
            1
        )
    def test3(self):
        self.assertEqual(
            find(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]),
            3
        )

def find(n, trust):
    survey = {}
    count = {}

    if n == 1:
        return 1

    for i in range(n):
        survey[i+1] = []

    for i in trust:
        survey[i[0]].append(i[1])
 
    for _, v in survey.items():
        for num in v:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

    for _, v in count.items():
        if n-1 == v:
            for k, v in survey.items():
                if len(v) == 0:
                    return k
    return -1

if __name__ == "__main__":
    unittest.main()