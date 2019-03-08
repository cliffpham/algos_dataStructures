class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.input.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        
        if self.output:
            i = len(self.output)-1
            return self.output[i]
        else:
            return self.input[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        if len(self.input) > 0 or len(self.output) > 0:
            return False

        return True
