import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            mcw("a, a, a, a, b,b,b,c, c", ["a"]),
            "b"
        ),
    def test2(self):
        self.assertEqual(
            mcw(("Bob, HIt, bAll"), ["bob", "hit"]),
            "ball"
        )

def mcw(paragraph, banned):
    paragraph = paragraph.split()
    seen = {}
    max_val = 0
    most_common_word = None

    for word in paragraph:
        word = word.strip("!?',;.")
        word = word.lower()
        char_list = word.split(',')
      
        for char in char_list:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
                if char in banned:
                    del seen[char]

        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1
            if word in banned:
                del seen[word]

        for k, v in seen.items():
            if v > max_val:
                most_common_word = k
                max_val = v
                
    return most_common_word

if __name__ == "__main__":
    unittest.main()