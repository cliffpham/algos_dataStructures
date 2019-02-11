def four_sum(nums, target, i, cur, output):
    if len(cur) == 4:
        if sum(cur) == target:
            c = sorted(cur)
            if c not in output: 
                output.append(c[:])
        return 
    
    if i == len(nums):
        return output
    
    four_sum(nums, target, i+1, cur, output)

    cur.append(nums[i])
    four_sum(nums, target, i+1, cur, output)
    cur.pop()

    return output

# print(four_sum([1,0,-1,0,-2,2], 0, 0, [], []))
# print(four_sum([], 0, 0, [], []))
# print(four_sum([-3,-2,-1,0,0,1,2,3], 0, 0, [], []))
print(four_sum([-5,5,4,-3,0,0,4,-2], 4, 0, [], []))
