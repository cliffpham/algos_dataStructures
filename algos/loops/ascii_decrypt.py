import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            decrypt('dnotq'),
            'crime'
        ),
    def test2(self):
        self.assertEqual(
            decrypt('flgxswdliefy'),
            'encyclopedia'
        )

def decrypt(word):
    secondStep = 1
    decryption = ""

    for i in range(len(word)):
        new_letter_ascii = ord(word[i])
        new_letter_ascii = new_letter_ascii - secondStep

        while new_letter_ascii < ord('a'):
            new_letter_ascii += 26
        
        decryption += str(chr(new_letter_ascii))
        secondStep += new_letter_ascii

    return decryption

if __name__ == "__main__":
    unittest.main()



