import unittest


class test_reverse_integer(unittest.TestCase):
    def test1_reverse_integer(self):
        self.assertEqual(
            reverse_integer(4562),
            2654
        )
    def test2_reverse_integer(self):
        self.assertEqual(
            reverse_integer(120),
            21
        )
    def test3_reverse_integer(self):
        self.assertEqual(
            reverse_integer(-984572387),
            -783275489
        )

def reverse_integer(n):
    reverse_num = 0
    is_negative = False
            
    if n < 0:
        is_negative = True
        n *= -1
        
    while n:
        reverse_num = reverse_num * 10 + (n % 10)
        n = n // 10
                
    if is_negative:
        reverse_num *= -1
                
    if reverse_num < (-2**31) or reverse_num > (2**31)-1:
        return 0
    
    return reverse_num

if __name__ == "__main__":
    unittest.main()


