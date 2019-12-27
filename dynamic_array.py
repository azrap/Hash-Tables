class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None]*capacity  # allocate memory

    def insert(self, index, value):
        if self.count >= self.capacity:
            # TODO: make array resize
            self.double_size()
        # shift everything at index to the right
        if index > self.count:
            print("ERROR: Out of range")
            return
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        self.storage[index] = value
        self.count += 1

    def delete(self, index):
        if index >= self.count:
            print("ERROR: Out of range")
            return

        # Shift everything to the left
        for i in range(index, self.count-1, 1):
            self.storage[i] = self.storage[i+1]

        self.count -= 1

    def append(self, value):
        self.insert(self.count, value)

    def prepend(self, value):
        self.insert(0, value)
        print(value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None]*self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


my_array = DynamicArray(3)
print(my_array.count)
my_array.insert(0, 5)
my_array.insert(0, 4)
my_array.insert(0, 15)
my_array.insert(1, 25)
my_array.append(30)
my_array.prepend(30)

print(my_array.storage)
