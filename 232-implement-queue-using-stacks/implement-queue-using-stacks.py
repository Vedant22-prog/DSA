class MyQueue(object):

    def __init__(self):
        self.inputStack = []
        self.outputStack = []

    def push(self, x):
        self.inputStack.append(x)

    def pop(self):
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())

        return self.outputStack.pop()

    def peek(self):
        if not self.outputStack:
            while self.inputStack:
                self.outputStack.append(self.inputStack.pop())

        return self.outputStack[-1]

    def empty(self):
        return len(self.inputStack) == 0 and len(self.outputStack) == 0