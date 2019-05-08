class Node:
    def __init__(self, data):
        self.data = data
        self.next = data
        self.prev = data

class Head:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = "Head"

class Tail:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = "Tail"

class DoublyLinkedList:
    def __init__(self):
        self.head = Head()
        self.tail = Tail()

    def insert_initial_node(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = self.tail
        self.tail.next = new_node

    def insert_node(self, data):
        if not self.head.prev:
            self.insert_initial_node(data)
        else:
            new_node = Node(data)
            prev_node = self.head.prev

            new_node.next = self.head
            self.head.prev = new_node
            prev_node.next = new_node
            new_node.prev = prev_node

    def traverse_forward(self, node):
        print("Traversal From the Head to the Tail")
        while node:
            print(" %s" %(node.data))
            last = node
            node = node.prev

    def traverse_backward(self, node):
        print("Traversal From the Tail to the Head")
        while node:
            print(" %s" %(node.data))
            last = node
            node = node.next

linked_list = DoublyLinkedList()
linked_list.insert_node('A')
linked_list.insert_node('B')
linked_list.insert_node('C')
linked_list.traverse_forward(linked_list.head)
linked_list.traverse_backward(linked_list.tail)
