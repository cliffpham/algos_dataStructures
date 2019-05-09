import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            solve(38),
            2
        )
#recursive solution 8ms    
def recur(num, total):
    if num < 9:
        return num + total
    return recur(num // 10, total + num % 10)

def solve(num):
    total = 0
    while num > 9:
        num = recur(num, total)
    return num

#iterative solution 20ms
#def repeat(num):
#    num = str(num)
#    result = 0
#    for i in range(len(num)):
#        result += int(num[i])
#    return result
#
#def solve(num):
#    while num > 9:
#        num = repeat(num)
#    return num

if __name__ == "__main__":
    unittest.main()
