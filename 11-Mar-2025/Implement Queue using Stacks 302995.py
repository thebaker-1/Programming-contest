# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.i = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        index = self.i
        self.i += 1
        return self.stack[index]
        

    def peek(self) -> int:
        return self.stack[self.i]
        

    def empty(self) -> bool:
        return (len(self.stack) - self.i) <= 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()