import unittest

class atoi_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            atoi('   -42'),
            -42
        )
    def test2(self):
        self.assertEqual(
            atoi('-91283472332'),
            -2147483648
        )
    def test3(self):
        self.assertEqual(
            atoi('words and 987'),
            0
        )
    def test4(self):
        self.assertEqual(
            atoi('4193 with words 213'),
            4193
        )
    def test5(self):
        self.assertEqual(
            atoi(""),
            0
        )
def atoi(s):
    pointer = 0;
    is_negative = False
    solution = 0;

    while pointer < len(s) and ord(s[pointer]) < 33:
        pointer += 1
    
    if pointer < len(s):
        if s[pointer] == '-':
          is_negative = True
          pointer += 1 
        elif s[pointer] == '+':
          is_negative = False
          pointer += 1

    for pointer in range(pointer, len(s)):
        if not(ord(s[pointer]) >= 48 and ord(s[pointer]) <= 57):
            return solution
        else:
            solution *= 10
            solution += int(s[pointer])

    if is_negative:
        solution *=  -1

    if solution > 2**31 - 1:
        return 2**31 - 1 

    if solution < -2 ** 31:
        return  -2 ** 31
    
    return solution

if __name__ == "__main__":
    unittest.main()


