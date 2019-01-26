class Queue(object):
    def __init__(self):
        self.input_stack = []
        self.output_stack = []
    
    def enqueue(self, element):
        self.input_stack.append(element)
    
    def dequeue(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

# q = Queue()
# arr = ['c', 'a', 't']
# for i in range(3):
#     q.enqueue(arr[i])
# for i in range(3):
#     print(q.dequeue())
