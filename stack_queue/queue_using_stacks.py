# Problem: Implement queue using stack
# Link: https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: easy
# Approach: Queue


class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
        return self.stack2[-1]
        

    def empty(self):
        return max(len(self.stack), len(self.stack2)) == 0
        
# Time: Amortized(1)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()