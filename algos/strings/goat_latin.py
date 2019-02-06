import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            toGoatLatin("I speak Goat Latin"),
            "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        )
    def test2(self):
        self.assertEqual(
            toGoatLatin("The quick brown fox jumped over the lazy dog"),
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
        )

def toGoatLatin(S):
    S = queue_ify(S.split(' '))
    result = []
    
    while S:
        word = S.pop()
        word = scan(word)
        result.append(word)
        
    for i in range(len(result)):
        result[i] = add_a(i, result[i])
        
    return ' '.join(result)

def queue_ify(S):
    q = []
    while S:
        q.append(S.pop())
    return q

def scan(w):
    w = list(w)
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    if w[0] not in vowels:
        w.append(w[0])
        w.append('ma')
        w.pop(0)
    else:
        w.append('ma')
    
    return ''.join(w)

def add_a(i, w):
    w = w
    for a in range(i+1):
        a = 'a'
        w += a
 
    return w

if __name__ == "__main__":
    unittest.main()