import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve('(()()(())'),
            1
        ),
    
    def test2(self):
        self.assertEqual(
            solve(')('),
            2
        ),
    
    def test3(self):
        self.assertEqual(
            solve('()))(('),
            4
        ),
    def test4(self):
        self.assertEqual(
            solve('()'),
            0
        )

def que_ify(s):
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
    result = []

    while arr:
        result.append(arr.pop())
    return result

def solve(brackets):
    brackets = que_ify(brackets)
    stack = []

    while brackets:
        cur = brackets.pop()
        if cur == '(':
            stack.append(cur)
            print(stack)

        elif cur == ')' and '(' in stack:
            stack.pop()
        else:
            stack.append(cur)

    return len(stack)

if __name__ == "__main__":
    unittest.main()