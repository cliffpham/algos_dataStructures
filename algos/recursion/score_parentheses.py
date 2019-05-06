def calculate(count_stack, total):
    while count_stack:
        cur = count_stack.pop()
        if cur == 1:
            total += cur
        else:
            total *= 2
            break
    return total
    
def solve(s):
    s = list(s)
    stack = []
    count_stack = []
    total = 0
    
    for item in s:
        if item == '(' and len(stack) == 0:
            stack.append(item)
        
        elif item == '(' and len(stack) >= 1:
            stack.pop()
            stack.append(item)
            count_stack.append('*')
        
        elif item == ')' and len(stack) > 0:
            stack.pop()
            count_stack.append(1)
            
        else:
            total = calculate(count_stack, total)
    
    if count_stack > 0:
        total = calculate(count_stack, total)
         
    return total
