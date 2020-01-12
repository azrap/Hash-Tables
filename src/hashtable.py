# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_value = 5381
        # bit-shift and sum value for each character
        for char in key:
            hash_value = ((hash_value << 5)+hash_value) + char

        return hash_value

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # step1 _hash_mod the key to get an integer between 0 and self.capacity
        index = self._hash_mod(key)

        # step 2: check for collisisions
        if self.storage[index]:
            print(
                f"WARNING: there's already a key, value present at index {index} ")

        self.storage[index] = LinkedPair(key, value)

        print(self.storage[index].key)

        return self

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # 2 we check to see if anything is there in self.storage at that index

        if self.storage[index] and self.storage[index].key == key:
            self.storage[index] = None
            return "success"

        return "warning: the key was not found in the hashTable"

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # 1 we hash the key to find the index at which it ought to be stored
        index = self._hash_mod(key)

        # 2 we check to see if anything is there in self.storage at that index

        return self.storage[index].value

        # 3 if something is there, we loop down the linkedlist and return the key/value pair if it is stored there
        # 4 if it's not stored anywhere return None

    def resize(self):
        self.capacity *= 2
        new_storage = [None]*self.capacity

        for item in self.storage:
            if item is not None:
                new_index = self._hash_mod(item.key)
                new_storage[new_index] = LinkedPair(item.key, item.value)

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(10)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
