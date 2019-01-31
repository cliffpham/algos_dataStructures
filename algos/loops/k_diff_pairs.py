def k_diff(nums, k):
    nums.sort()
    i = 0
    j = 1
    counter = 0
    seen = set()

    while j < len(nums):
        diff = nums[j] - nums[i]
        if diff == k and (nums[j], nums[i]) not in seen and j != i:
            seen.add((nums[j],nums[i]))
            counter += 1
            i += 1
            j += 1
            
        elif diff > k:
            i += 1
        else:
            j += 1
   
    return counter


print(k_diff([3,1,4,1,5], 2))
print(k_diff([1,2,3,4,5], 1))
print(k_diff([1,1,1,1,2], 0))

# bruteforce

# def k_diff(nums, k):
#     result = []
    
#     for i in range(len(nums)):
#         for j in range(i+1 , len(nums)):
#             if nums[i] > nums[j]:
#                 if nums[i] - nums[j] == k:
#                     if (nums[i], nums[j]) in result: continue
#                     result.append((nums[i],nums[j]))
#             else:
#                 if nums[j] - nums[i] == k:
#                     if (nums[j], nums[i]) in result: continue
#                     result.append((nums[j],nums[i]))
#     return len(result)