def all_products_except(arr):
    """
    >>> all_products_except([1,7,3,4])
    [84, 12, 28, 21]


    """
    result = []
    for i in range(len(arr)):
        result.append(product_till(arr,i,0,1,{}) * product_to(arr,i,i+1,1,{}))
    return result

def product_till(arr, n, i, val, cache):
    if i in cache:
        return cache[i]

    if i == n:
        return val

    result = product_till(arr, n, i+1, val * arr[i], cache)
    cache[i] = result
    
    return result

def product_to(arr, n, i, val, cache):
    if i in cache:
        return cache[i]
    
    if i == len(arr):
        return val
    
    result = product_to(arr, n, i+1, val * arr[i], cache)
    cache[i] = result

    return result


