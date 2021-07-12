class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, val: int) -> None:
        if not self.q:
            curr_min = val
        else:
            curr_min = min(val, self.getMin())
        self.q.append((val, curr_min))

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()