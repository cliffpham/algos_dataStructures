def all_subsets(arr, i, cur, output):
    
    if i == len(arr):
        if len(cur) > 0:
            output.append(cur[:])
        return 

    all_subsets(arr, i+1, cur, output)

    cur.append(arr[i])
    all_subsets(arr, i+1, cur, output)
    cur.pop()

    return output

