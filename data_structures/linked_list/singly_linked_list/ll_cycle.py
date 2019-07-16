# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def solve(head):
    if not head:
        return False

    seen = set()
    cur = head
    while cur is not None:
        if cur not in seen:
            seen.add(cur)
        else:
            return True
        cur = cur.next
    return False
