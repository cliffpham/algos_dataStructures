# i need to know the instance of where the good suffix begins and ends
# create case 1, 2, 3

def find_good_suffix(text, pattern, pointer):
    start = pointer + (len(pattern) - 1)
    end = start - (len(pattern) - 1)
    j = len(pattern) - 1
    for i in range(start, end, -1):
        if text[i] != pattern[j]:
            return [i, j]
        j -= 1
    return -1

def case_one(pattern, cur, compare, window):
    count = 0
    for i in range(cur, -1, -1):
        start = i - len(window) + 1
        if pattern[start:i+1] == window:
            #check if the character before the start of the match differs from compare
            if pattern[i-len(window)] != compare:
                return count + len(window)
        count += 1
    return -1

# chop off the first character in the window and subsequently search for a matching section
def find_prefix(pattern, cur, suffix):
    count = 0
    for i in range(cur, -1, -1):
        start = i - len(suffix) + 1
        if pattern[start:i+1] == suffix:
            return count + len(suffix) + 1
        count += 1
    return -1

def case_two(pattern, cur, window):
    j = 0
    suffix = window[j:]
    while len(suffix) > 0:
        test = find_prefix(pattern, cur, suffix)
        if test != -1:
            return test
        else:
            j += 1
            suffix = window[j:]
    return False

def solve(text, pattern):
    end = "end of function"
    pointer = 0
    good_suffix = find_good_suffix(text, pattern, pointer)
    # compare is the character that differs in the pattern
    cur = good_suffix[1]
    compare = pattern[cur]
    window = pattern[cur+1:]
    
    test = case_one(pattern, cur, compare, window)
    if test != -1:
        return test
    else:
        test = case_two(pattern, cur, window)
        return test    
    return end

#text= "ABAABABACBA"
#pattern = "CABAB"
#text = "AABABABACBA"
#pattern = "ABBAB"
text = "AABABCA"
pattern = "BCCAB"
print(solve(text, pattern))
