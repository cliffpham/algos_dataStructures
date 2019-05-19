# bad char ==
# good char ==

# in solve: 
#if the return for searching for a bad character returns False (-1)
# then this means there was a continous substring match so we can skip that section of the string

# in the find_match function:
# if a bad charcter was found, we take the position of where it is in the original string and 
# where it is in the pattern to determine how many position (indexes) to move forward
# the distance is measured in the count

def find_mismatch(text, pattern, pointer):
    start = pointer + (len(pattern) - 1)
    till = start - (len(pattern)-1)
    j = len(pattern) - 1
    for i in range(start, till, -1):
        if text[i] != pattern[j]:
            return [i,j]
        j -= 1
    return -1

def find_match(text, pattern, bad_char):
    count = 0
    found = False
    for i in range(bad_char[1], -1, -1):
        if text[bad_char[0]] == pattern[i]:
            found = True
            break
        count += 1
    if found:
        return count
    return -1
            
def solve(text, pattern):
    pointer = 0
    result = []

    while pointer <= len(text) - len(pattern):
        bad_char = find_mismatch(text, pattern, pointer)
        if bad_char != -1:
            next_position = find_match(text, pattern, bad_char)
            if next_position == -1:
                pointer += len(pattern)
            else:
                pointer += next_position
        else:
            result.append(pointer)
            pointer = pointer + (len(pattern) - 1)
            
    return result
