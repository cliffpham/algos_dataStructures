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

    while len(left) < left_index and len(right) > right_index:
        if left[left_index] < right[right_index]:
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