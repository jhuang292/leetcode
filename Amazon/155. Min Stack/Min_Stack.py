class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.minStack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.val.append(x)
        if(len(self.minStack) == 0 or x <= self.minStack[-1]):
            self.minStack.append(x)
        
        

    def pop(self):
        """
        :rtype: void
        """
        if(len(self.val) == 0):
            return 
        else:
            if(self.val[-1] == self.minStack[-1]):
                self.minStack.pop()
            self.val.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if(len(self.val) == 0):
            return None
        return self.val[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.minStack) == 0):
            return None
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
