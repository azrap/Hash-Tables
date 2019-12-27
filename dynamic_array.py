class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None]*self.capacity  # allocate memory

    def insert(self, index, value):
        if self.count >= self.capacity:
            # TODO: make array resize
            print("ERROR: Array is full")
        # shift everything at index to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1
