from ll import *

def solve(head, m, n):
    if m == n:
        return head
    if not head or not m or not n:
        return None

    temp = Node(0)
    temp.next = head
    start = temp
    for _ in range(m - 1):
        start = start.next

    end = start.next
    cur = start.next
    prev = None

    for _ in range(n - m + 1):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    start.next = prev
    end.next = cur


#ll = Linked_List()
#ll.push('1')
#ll.push('2')
#ll.push('3')
#ll.push('4')
#ll.push('5')
#ll.print_list()
#solve(ll.head, 2, 4)
#ll.print_list()
