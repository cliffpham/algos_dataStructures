import itertools

def find_words(arr):
    result = []

    arr = letter_combinations(arr)
    dictionary = create_dictionary()
    result = check_dictionary(arr, dictionary)
    
    print(str(len(result)) + ' word(s) can be created: ', end='')
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
    
print(find_words(['a','t','o','c','r','y']))
print(find_words(['a','t','p','c','z']))
