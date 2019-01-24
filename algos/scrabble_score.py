import itertools

def scrabble_score(arr):
    arr = find_words(arr)
    scrabble_values = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    
    max_val = 0
    best_word = None
    
    for word in arr:
        current_word = 0
        
        for letters in word:
            current_word += scrabble_values[letters]
            if current_word > max_val:
                best_word = word
            max_val = max(max_val, current_word)
    
    print('The highest scoring word is ' + best_word + ' with a value of ', end='')
    return max_val

def find_words(arr):
    result = []

    arr = letter_combinations(arr)
    dictionary = create_dictionary()
    result = check_dictionary(arr, dictionary)
    
    return result

def letter_combinations(arr):
    perms = []
    for r in range(len(arr)):
        perms += [''.join(s) for s in itertools.permutations(arr, r)]
        
    return perms

def create_dictionary():
    words = '/usr/share/dict/words'
    dictionary = set()
    with open(words, 'r') as wf:
        words = wf.readlines()
    for word in words:
        dictionary.add(word.strip())

    return dictionary

def check_dictionary(arr, dictionary):
    result = []
    for i in arr:
        if i in dictionary:
            if len(i) > 1:
                result.append(i)
    return result

print(scrabble_score(['a', 'c', 't', 'z', 'p','y','d']))
print(scrabble_score(['t', 'r', 's', 'z', 'p', 'o', 'x']))