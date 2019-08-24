class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None, 'Head')
        self.tail = Node(None, 'Tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get_least_used(self):
        return self.head.next


class LRU:
    def __init__(self, n):
        self.n = n
        self.dict = {}
        self.list = LinkedList()

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]
        else:
            return -1

        self.list.remove(n)
        self.list.add(n)

        return n.val
    
    def put(self, key, val):
        if key in self.dict:
            n = self.dict[key]
            self.list.remove(n)
            del self.dict[key]

        n = Node(key, val)
        self.list.add(n)
        self.dict[key] = n

        if len(self.dict) > self.n:
            to_remove = get_least_used()
            self.list.remove(to_remove)
            del self.dict[to_remove.key]


