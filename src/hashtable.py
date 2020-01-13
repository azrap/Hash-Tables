# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, LinkedPair=None):
        self.head = LinkedPair
        self.tail = LinkedPair


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

        # # step 0, check to see if there are any cells that are empty
        # resize = True
        # for item in self.storage:
        #     # break the loop if there's an empty cell
        #     if item is None:
        #         resize = False
        #         break
        # # if there aren't any empty cells, resize:
        # if resize is True:
        #     self.resize()

        # step 1, _hash_mod the key to get an integer between 0 and self.capacity
        index = self._hash_mod(key)

        # link the key, value together for storage:
        linked_pair = LinkedPair(key, value)

        # step 2: store the linked pair
        if self.storage[index]:
            # if collision, store the lp at the tail of the existing ll
            if self.retrieve(key):
                linked_list = self.storage[index]
                current = linked_list.head
                while current:
                    if current.key == key:
                        current.value = value
                    current = current.next

            else:
                linked_list = self.storage[index]
                linked_list.tail.next = linked_pair
                linked_list.tail = linked_pair

        else:
            # else store the lp in a new ll at the index
            self.storage[index] = LinkedList(linked_pair)

        return self

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        linked_pair_value = self.retrieve(key)
        index = self._hash_mod(key)
        linked_list = self.storage[index]

        if linked_pair_value:
            current = linked_list.head
            prev = current

            # if there's only one linked_pair in the list
            if current == linked_list.head and current == linked_list.tail:
                # set the storage to None to remove the list
                self.storage[index] = None
                return True
            # else if the head has the key we want to remove:
            elif current.key == key:
                linked_list.head = current.next
                current.next = None
                return True
            else:
                print('current value', current.value)
                print('prev value', prev.value)
                while current:
                    if current.key == key:
                        if linked_list.tail == current:
                            linked_list.tail = prev
                        prev.next = current.next
                        current.next = None
                        return True
                    prev = current

                    current = current.next
        return "bleep"

        # 2 we check to see if anything is there in self.storage at that index

        # if self.storage[index]:
        #     linked_list = self.storage[index]
        #     # if there is only one linked pair in the list
        #     if linked_list.head == linked_list.tail:
        #         if linked_list.head.key == key:
        #             self.storage[index] = None
        #             return True
        #         else:
        #             return False
        #     # if there is more than one linked pair in the list
        #     current = linked_list.head
        #     prev = current
        #     while current:
        #         if current.key == key:
        #             if current.next == linked_list.tail:
        #                 linked_list.head = linked_list.tail
        #                 current.next = None
        #                 return f"deleted ({current.key}, {current.value}) from storage"
        #         prev = current
        #         current = current.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # 1 we hash the key to find the index at which it ought to be stored
        index = self._hash_mod(key)

        # 2 we check to see if anything is there in self.storage at that index

        linked_list = self.storage[index]

        if linked_list:
            current = linked_list.head
            while current:
                if current.key == key:
                    return current.value
                current = current.next

        return None

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
    ht = HashTable(3)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # print(ht.remove("line_3"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
