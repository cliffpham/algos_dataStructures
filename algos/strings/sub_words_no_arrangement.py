def sub_words(s):
    first_index = 0
    last_index = len(s) - 1
    possible_words = []

    words = '/usr/share/dict/words'
    dictionary = set()
    with open(words, 'r') as wf:
        words = wf.readlines()
    for word in words:
        dictionary.add(word.strip())

    while first_index < last_index:
        cur = ''
        for i in range(first_index, len(s)):
            cur += s[i]
            if cur in dictionary: 
                if len(cur) > 1:
                    possible_words.append(cur)
        first_index += 1

    return possible_words

print(sub_words('sadmonkey'))


    
    
    
