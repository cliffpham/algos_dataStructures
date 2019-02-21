#incomplete

def palindrome(s):
    pivot = 1
    new_str = convert_str(s)
    count = 0
    flag = True
    seen = dict()
    result = []
    
    while pivot < len(new_str)-1:
        if new_str[pivot-1] != new_str[pivot+1]:
            result.append(count)
            pivot += 1
            
        else:
            l = pivot - 1
            r = pivot + 1
            sub_string = '' + new_str[pivot]
            while flag:
                if new_str[l] == new_str[r]:
                    if new_str[l] != '#':
                        sub_string += new_str[r] #either l or r works
                    count += 1
                    l -= 1
                    r += 1
                else:
                    result.append(count)
                    # print(sub_string)
                    # if sub_string not in seen:
                    #     seen[sub_string] = count
                    count = 0
                    flag = False
            pivot += 1
            flag = True
    print(result)  
    return find_all_substrings(seen)

def find_all_substrings(seen):
    combine = []

    for i in seen:
        combine.append(seen[i])
    
    return sum(combine)

def convert_str(s):
    s = '#'.join(s)
    s = '#' + s + '#'
    s = '^' + s + '$'
    
    return s
    
print(palindrome("fdsklf"))
print(palindrome('aaa'))

