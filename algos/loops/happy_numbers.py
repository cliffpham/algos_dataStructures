import unittest

class test_happy_num(unittest.TestCase):
    def test1(self):
        self.assertTrue(
            happy_numbers(7)
        )
    def test2(self):
        self.assertFalse(
            happy_numbers(201)
        )

def happy_numbers(n):
    result = find_happy(n)
    hist = {}

    while result > 1:
        hist[result] = result
        result = find_happy(result)
        if result in hist:
            break
       
    return result == 1

def find_happy(n):
    result = 0
    while n:
        result += (n%10) ** 2
        n = n // 10
    
    return result

if __name__ == "__main__":
    unittest.main()

#     result = recur(n)
#     hist = {}
#     loop = [result]

#     while result > 1:
#         hist[result] = result
#         result = recur(result)
#         loop.append(result)
#         if result in hist:
#             for i in range(len(loop)): 
#                 if loop[i] == result:
#                     print(loop[i:])
#                     break
#             break

#     return result == 1

# def recur(n):
#     n = str(n)
#     s = 0
    
#     for i in range(len(n)):
#         s += (int(n[i]) * int(n[i]))

#     return s

# for i in range(1,1001):
#     print(i, happy_numbers(i))
# print(happy_numbers(12))
# print(happy_numbers(11))




