# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def solve(head):
    arr = []
    cur = head

    while cur is not None:
        arr.append(cur.val)
        cur = cur.next

    return arr == arr[::-1]
