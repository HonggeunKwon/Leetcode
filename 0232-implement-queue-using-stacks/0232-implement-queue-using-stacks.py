class MyQueue:

    def __init__(self):
        self.left = []
        self.right = []

    def push(self, x: int) -> None:
        self.left.append(x)

    def pop(self) -> int:
        self.peek()
        return self.right.pop()

    def peek(self) -> int:
        if not self.right:
            while self.left:
                self.right.append(self.left.pop())
        return self.right[-1]

    def empty(self) -> bool:
        return len(self.right) == 0 and len(self.left) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()