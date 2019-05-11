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
    
    def find_node(self, node):
        found = False
        start = self.head
        while start:
            if start.data == node:
                found = True
                break
            last = start
            start = start.prev
        if found:
            print ("Node of value: " + node + " was found")
        else:
            print ("No node with value: " + node + " was found")
    
    def delete_node(self, node):
        found = False
        start = self.head
        while start:
            if start.data == node:
                left_node = start.next
                right_node = start.prev
                left_node.prev = right_node
                right_node.next = left_node
                found = True
                break
            last = start
            start = start.prev
        if found:
            print ("Node was removed")
        else:
            print ("Node was not found")
        return start

    def pop_left(self):
        to_pop = self.head.prev
        if not to_pop:
            print ("Linked List is empty")
        return self.delete_node(to_pop.data)

    def pop_right(self):
        to_pop = self.tail.next
        if not to_pop:
            print("Linked List is empty")
        return self.delete_node(to_pop.data)

    def push(self, data):
        self.insert_node(data)
        print ("Inserted node")
                
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

#linked_list = DoublyLinkedList()
#linked_list.insert_node('A')
#linked_list.insert_node('B')
#linked_list.insert_node('C')
#linked_list.insert_node('D')
#linked_list.insert_node('E')
#linked_list.insert_node('F')
#linked_list.traverse_forward(linked_list.head)
## linked_list.traverse_backward(linked_list.tail)
#linked_list.find_node('B')
#linked_list.delete_node('D')
#linked_list.pop_left()
#linked_list.traverse_forward(linked_list.head)
#linked_list.push('G')
#linked_list.pop_right()
#linked_list.traverse_forward(linked_list.head)
