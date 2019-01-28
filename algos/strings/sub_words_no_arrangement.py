def sub_words(s):
    first_index = 0
    last_index = len(s) - 1
    possible_words = []
    dictionary = create_dictionary()

    while first_index < last_index:
        cur = ''
        for i in range(first_index, len(s)):
            cur += s[i]
            if cur in dictionary: 
                if len(cur) > 1:
                    possible_words.append(cur)
        first_index += 1

    print(str(len(possible_words)) + ' word(s) can be created: ', end='')
    return possible_words

def create_dictionary():
    words = '/usr/share/dict/words'
    dictionary = set()
    with open(words, 'r') as wf:
        words = wf.readlines()
    for word in words:
        dictionary.add(word.strip())

    return dictionary

# print(sub_words('supercalifragilisticexpialidocious'))


    
    
    
