def happy_numbers(n):
    result = recur(n)
    hist = {}
    loop = [result]

    while result > 1:
        hist[result] = result
        result = recur(result)
        loop.append(result)
        if result in hist:
            for i in range(len(loop)):
                if loop[i] == result:
                    print(loop[i:])
                    break
            break

    return result == 1

def recur(n):
    n = str(n)
    s = 0
    
    for i in range(len(n)):
        s += (int(n[i]) * int(n[i]))

    return s

# for i in range(1,1001):
#     print(i, happy_numbers(i))
# print(happy_numbers(12))



