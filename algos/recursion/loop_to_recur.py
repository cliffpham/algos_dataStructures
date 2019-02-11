# loop_sum
# acc = 0;
# for i = 0; i < 100; i++:
#     acc += i

def recur_add(n, i, acc):
    if i == n:
        return acc
    acc += i
    return recur_add(n, i+1, acc)

# print(recur_add(100, 0, 0))

#loop_product
# acc = 1
# for i = 100; i > 0; i--:
#     acc *= i

def multiply(n):
    acc = 1
    for i in range(n, 1, -1):
        acc *= i

    return acc

# print(multiply(5))

def multiply_recur(n, acc=1):
    if n == 0:
        return acc

    acc *= n

    return multiply_recur(n-1, acc)
    

# print(multiply_recur(5))

# def recur_multiply(n, acc = 1):
#     if n < 0:
#         return 0
#     j = 0
#     while j < n:
#         print(acc, (n*j))
#         acc += (n*j)
#         j += 1
        
#     return acc + recur_multiply(n-1)

# print(recur_multiply(5))

# nested_loops
# acc = 1
# for i = 100; i > 0; i--:
#     for j = 0; j < 100; j++:
#       acc += (i * j)

def nested_loops(n):
    acc = 1
    for i in range(n, -1, -1):
        for j in range(i):
            print(acc, i, j)
            acc += i * j
        
    return acc

def recur_nested(n, j, acc=1):
   
    if n == 0:
        return acc
    
    if j == n:
        return recur_nested(n-1, 0, acc)
    
    acc += (n*j)
    print(acc, n, j)
    
    return recur_nested(n, j+1, acc)

# def recur_nested(n, i, j, acc=1):
#     # print(i, j)

#     if i < 0:
#         return acc
    
#     acc += (i * j)

#     if j < 5:
#         return recur_nested(i, j+1, acc)
    
#     else:
#         return recur_nested(i-1, 0, acc)
    
print(recur_nested(5,0))
print('**************')
print(nested_loops(5))
