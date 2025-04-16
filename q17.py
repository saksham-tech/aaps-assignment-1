class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, val):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow")
            return
        self.top1 += 1
        self.arr[self.top1] = val

    def push2(self, val):
        if self.top1 + 1 == self.top2:
            print("Stack Overflow")
            return
        self.top2 -= 1
        self.arr[self.top2] = val

    def pop1(self):
        if self.top1 == -1:
            print("Stack Underflow for Stack 1")
            return
        val = self.arr[self.top1]
        self.top1 -= 1
        return val

    def pop2(self):
        if self.top2 == self.size:
            print("Stack Underflow for Stack 2")
            return
        val = self.arr[self.top2]
        self.top2 += 1
        return val
        
#TIME COMPLEXITY = O(1)
#SPACE COMPLEXITY = O(N)