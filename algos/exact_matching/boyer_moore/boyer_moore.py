def find_mismatch(text, pattern, pointer):
    start = pointer + (len(pattern) - 1)
    till = start - (len(pattern)-1)
    j = len(pattern) - 1
    for i in range(start, till-1, -1):
        if text[i] != pattern[j]:
            return [i,j]
        j -= 1
    return -1

def find_match(text, pattern, bad_char):
    bad_count = 0
    good_count = 0
    found = False
    cur = bad_char[1]
    compare = pattern[cur]
    window = pattern[cur+1:]

    suffix = case_one(pattern, cur, compare, window)
    if good_count != -1:
        good_count += suffix
    else:
        good_count += case_two(pattern, cur, window)

    for i in range(bad_char[1], -1, -1):
        if text[bad_char[0]] == pattern[i]:
            found = True
            break
        bad_count += 1
    if found:
        return max(bad_count, good_count)
    return -1

def case_one(pattern, cur, compare, window):
    count = 0
    for i in range(cur, -1, -1):
        start = i - len(window) + 1
        if pattern[start:i+1] == window:
            if pattern[i-len(window)] != compare:
                return count + len(window)
        count += 1
    return -1

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
    return -1

def solve(text, pattern):
    pointer = 0
    result = []

    while pointer <= len(text) - len(pattern):
        bad_char = find_mismatch(text, pattern, pointer)
        if bad_char != -1:
            next_position = find_match(text, pattern, bad_char)
            if next_position == -1:
                pointer += 1
            else:
                pointer += next_position
        else:
            result.append(pointer)
            pointer = pointer + (len(pattern) - 1)
    return result

print(solve("I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy.", "happy"))
print(solve("AABABCA", "BCCAB"))
print(solve("lookingforaneasteregg", "easter"))
