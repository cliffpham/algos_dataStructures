def pascal(n):
    result = recur(n, 0, [])
    return  result[1:len(result)+1]

def recur(n, i, prev):
    if i > n:
        return []
    if n == 0:
        return recur(n, i+1, [1])
  
    return [prev] + recur(n, i+1, calculate(prev))

def calculate(prev):
    prev = prev + [0]
    return [1] + [x+y for x,y in zip(prev[1:], prev[:-1])]

print(pascal(5))