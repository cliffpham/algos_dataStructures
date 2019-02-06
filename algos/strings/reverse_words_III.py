# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            reverse_sentence("Let's take LeetCode contest"),
            "s'teL ekat edoCteeL tsetnoc"
        )

def reverse_sentence(s):
    result = []
    s = queue_ify(s.split(' '))
    
    while s:
        w = s.pop()
        w = reverse_word(w)
        result.append(w)
    
    return ' '.join(result)

def queue_ify(arr):
    q = []
    while arr:
        q.append(arr.pop())
    return q

def reverse_word(w):
    w = list(w)
    l = 0
    r = len(w) - 1
    while l < r:
        temp = w[l]
        w[l] = w[r]
        w[r] = temp
        l += 1
        r -= 1
    return ''.join(w)

if __name__ == "__main__":
    unittest.main()

