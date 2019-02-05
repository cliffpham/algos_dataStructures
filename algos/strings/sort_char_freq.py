def frequent(s):
    count = {}
    new_str = ''

    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1

    for key in sorted(count, key=count.get, reverse=True):
        freq = count.get(key) 
        if freq > 1:
            for _ in range(freq-1):
                new_str += key
        new_str += key        

    return new_str

# print(frequent('Aabb'))
print(frequent('loveleetcode'))