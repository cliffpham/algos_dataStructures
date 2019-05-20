# i need to know the instance of where the good suffix begins and ends
# create case 1, 2, 3

def find_good_suffix(text, pattern, pointer):
    start = pointer + (len(pattern) - 1)
    end = start - (len(pattern) - 1)
    j = len(pattern) - 1
    for i in range(start, end, -1):
        if text[i] != pattern[j]:
           # print(pattern[j:])
            return [i, j]
        j -= 1
    return -1

def case_one(text, pattern, cur, compare, window):
    for i in range(cur, -1, -1):
        if i - len(window) < 0:
            start = 0
        else:
            start = i - len(window)
        print(pattern[i+1:])
        if pattern[i+1:] == window:
            print("i is currently at: " + str(i))
            #check if the character before the start of the match differs from compare
            print(pattern[i-len(window)])
            #print(pattern[i-len(window)] == compare)
            if pattern[i-len(window)] != compare:
                return True
    return False

def solve(text, pattern):
    end = "end of function"
    pointer = 0
    good_suffix = find_good_suffix(text, pattern, pointer)
    # compare is the character that differs in the pattern
    cur = good_suffix[1]
    compare = pattern[cur]
    window = pattern[cur+1:]

    print(case_one(text, pattern, cur, compare, window))

    return end

text= "ABAABABACBA"
pattern = "CABAB"
print(solve(text, pattern))
