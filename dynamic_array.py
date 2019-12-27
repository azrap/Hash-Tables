class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None]*self.capacity  # allocate memory

    def insert(self, index, value):
        if self.count >= self.capacity:
            # TODO: make array resize
            print("ERROR: Array is full")
            return
        # shift everything at index to the right
        if index > self.count:
            print("ERROR: Out of range")
            return
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1


my_array = DynamicArray(3)
my_array.insert(10, 3)
my_array.insert(0, 5)
my_array.insert(0, 4)
my_array.insert(0, 3)

print(my_array.storage)
