class MyStack:

    def __init__(self):
        self.q = collections.deque()
    
    def __len__(self):
        return len(self.q)

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        if len(self) > 0:
            return self.q.popleft()
        return -1

    def top(self) -> int:
        if len(self) > 0:
            return self.q[0]
        return -1

    def empty(self) -> bool:
        return len(self) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()