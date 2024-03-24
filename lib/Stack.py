class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
        pass

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item.")

        pass

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

        pass

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

        pass
    
    def size(self):
        return len(self.items)
        pass

    def full(self):
        return len(self.items) == self.limit
        pass

    def search(self, target):
        index = -1
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                index = len(self.items) - i - 1
                break
        return index
        pass
