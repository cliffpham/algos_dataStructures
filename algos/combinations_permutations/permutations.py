def recur(nums, i, cur, output, seen):
    if len(cur) == len(nums):
        output.append(cur[:])
        return output
    
    if i >= len(nums):
        return output
    
    recur(nums, i+1, cur, output, seen)
    
    if not i in seen:
        cur.append(nums[i])
        seen[i] = True
        recur(nums, 0, cur, output, seen)
        cur.pop()
        del seen[i]
    
    return output


def permute(nums):

    return recur(nums, 0, [], [], {})


# def perms(arr, i, cur, used):
#     for i in range(0, len(arr)):
#         if not i in used:
#             cur.append(arr[i])
#             used[i] = True
#             perms(arr, i, cur, used)
#             cur.pop()
#             del used[i]
#     print(cur)
   

# print(perms([1,2,3], 0, [], {}))


# def all_perm(arr, i, cur, used):
#     if len(cur) == len(arr):
#         print(cur)
#         return
    
#     if i >= len(arr):
#         return

#     all_perm(arr, i+1, cur, used)

#     if i not in used:
#         cur.append(arr[i])
#         used[i] = cur 
#         all_perm(arr, i+1, cur, used)
#         print(used)
#         del used[i]
#         print(used)
#         cur.pop()

    



# print(permute([1,2,3]))

# print(perms([1,2,3], 0, [], {}))