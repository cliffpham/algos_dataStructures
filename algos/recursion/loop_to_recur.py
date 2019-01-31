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

def recur_multiply(n, acc = 1):
    if n < 1:
        return acc
    acc *= n
    return recur_multiply(n-1, acc)

# print(recur_multiply(100))

#nested_loops
# acc = 1
# for i = 100; i > 0; i--:
#     for j = 0; j < 100; j++:
#       acc += (i * j)
def recur_nested(i, j, acc=1):
    if i < 0 and j > 100:
        return acc
    
    acc += (i * j)
    
    return recur_nested(i-1, j+1, acc)
# print(recur_nested(100,0))
