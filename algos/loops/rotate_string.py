def rotate_string(s, s2):
    # l = len(s)
    new_s = ''
    for i in range(len(s)):
        i = s
        new_s += i
   
    for i in range(len(new_s)):
        if new_s[i:i+len(s2)] == s2:
            return True

    return False
print(rotate_string('abcde', 'cdeab'))
print(rotate_string('abcde', 'abced'))