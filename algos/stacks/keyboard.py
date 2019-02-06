import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            keyboard(["Hello", "Alaska", "Dad", "Peace"]),
            ['Alaska', 'Dad']
        )

def keyboard(words):
    result = []
    words = queue_ify(words)
    while words:
        cur = words.pop()
        if check_top_keys(cur) or check_middle_keys(cur) or check_lower_keys(cur):
            result.append(cur)
    
    return result

def check_top_keys(word):
    top_keys = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    word = word.lower()
    for _, v in enumerate(word):
        if v not in top_keys:
            return False
    return True

def check_middle_keys(word):
    middle_keys = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    word = word.lower()
    for _, v in enumerate(word):
        if v not in middle_keys:
            return False
    return True

def check_lower_keys(word):
    lower_keys = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    word = word.lower()
    for _, v in enumerate(word):
        if v not in lower_keys:
            return False
    return True

def queue_ify(arr):
    q = []
    while arr:
        q.append(arr.pop())
    return q

if __name__ == "__main__":
    unittest.main()