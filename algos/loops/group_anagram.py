import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        ),
    def test2(self):
        self.assertEqual(
            solve(["", "b"]),
            [[''], ['b']]
        ),
    def test3(self):
        self.assertEqual(
            solve(["tao","pit","cam","aid","pro","dog"]),
            [['tao'], ['pit'], ['cam'], ['aid'], ['pro'], ['dog']]
        )

def solve(strs):
    chars = {}
    index = {}
    result = []
    count = 0
    counter2 = 0

    for word in strs:
        if len(word) == 0:
            chars[""] = count
            count += 1

        for l in range(len(word)):
            if word[l] not in chars:
                chars[word[l]] = count
                count += 1

    for word in strs:
        convert = list(word)

        for i,j in enumerate(convert):
            convert[i] = chars[j]
        
        convert.sort()
        convert = str(convert)
        
        if convert not in index:
            index[convert] = counter2
            result.append([word])
            counter2 += 1
        else:
            i = index[convert]
            result[i].append(word)

    return result

if __name__ == "__main__":
    unittest.main()