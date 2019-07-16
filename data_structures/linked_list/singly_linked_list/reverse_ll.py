from ll import *

def reverse(ll):
    current = ll.head
    prev = None

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    ll.head = prev

#ll = Linked_List()
#ll.push('A')
#ll.push('B')
#ll.push('C')
#ll.print_list()
#reverse(ll);
#ll.print_list()
