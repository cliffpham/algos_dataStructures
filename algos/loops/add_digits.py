import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            solve(38),
            2
        )

def repeat(num):
    num = str(num)
    result = 0
    for i in range(len(num)):
        result += int(num[i])
    return result

def solve(num):
    while num > 9:
        num = repeat(num)
    return num

if __name__ == "__main__":
    unittest.main()
