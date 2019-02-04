# space efficient solution

import math

def closet(points, K):
    output = []
    points = merge_sort(points)

    while len(output) < K:
        output.append(points.pop())

    return output

def compare(points, index):
    cur = points[index]
    return math.trunc(math.pow(cur[0],2) + math.pow(cur[1], 2))

#descending order merge sort
def merge_sort(arr):
    left_index = 0
    right_index = 0

    if len(arr) < 2:
        return arr

    left = arr[0:(len(arr)//2)]
    right = arr[len(arr)//2:len(arr)]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right, left_index, right_index)

def merge(left, right, left_index, right_index):
    results = []

    while len(left) > left_index and len(right) > right_index:
        if compare(left, left_index) < compare(right, right_index):
            results.append(right[right_index])
            right_index += 1
        else:
            results.append(left[left_index])
            left_index += 1

    while len(left) > left_index:
        results.append(left[left_index])
        left_index += 1

    while len(right) > right_index:
        results.append(right[right_index])
        right_index += 1

    return results

# print(closet(points = [[-5,4],[-6,-5],[4,6]], K=2))
# print(closet(points = [[3,3],[5,-1],[-2,4]], K=2))
# print(closet(points = [[-2,10],[-4,-8],[10,7],[-4,-7]], K=3))

# time efficient solution

def kClosest(points, K):
    points.sort(reverse = False, key = lambda p: p[0]**2 + p[1]**2)
    
    return points[:K]



