import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            generate_parentheses(3),
            ['((()))', '(()())', '(())()', '()(())', '()()()']
        )

def recur(cur, available, unclosed):
    if available == 0:
        # print('cur after available = 0: ', end='')
        # print([cur + ')' * unclosed])
        return [cur + ')' * unclosed]
    
    if unclosed == 0:
        # print('cur after unclosed = 0: ', end='')
        # print(cur)
        return recur(cur + '(', available-1, unclosed+1)

    l = recur(cur + '(', available-1, unclosed+1)
    r = recur(cur + ')', available, unclosed-1)

    return l + r

def generate_parentheses(n):
    if n == 0:
        return []
    return recur('', n, 0)

if __name__ == "__main__":
    unittest.main()
