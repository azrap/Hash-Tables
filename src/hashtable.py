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

        for char in key:
            # bit-shift and sum Unicode value for each character
            hash_value = ((hash_value << 5)+hash_value) + ord(char)

        return hash_value

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.

        '''

        index = self._hash_mod(key)

        # link the key, value together for storage:
        linked_pair = LinkedPair(key, value)

        # step 2: store the linked pair
        if self.storage[index]:
            # if collision, store the lp at the tail of the existing ll

            # if the key, value pair already exists:
            if self.retrieve(key):
                # get the linked list where it it is stored
                linked_list = self.storage[index]
                current = linked_list.head
                # go through each linked pair
                while current:
                    # if you find the key:
                    if current.key == key:
                        # replace the value and return the list
                        current.value = value
                        return self
                    # if not, keep moving down the list
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
            # if there's only one linked_pair in the list, head will equal tail
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

        for list in self.storage:

            if list is not None:

                current = list.head

                # while there are linked_pairs in linked_list
                while current:

                    # get the new index for each item
                    new_index = self._hash_mod(current.key)

                    # get the new linked pair
                    new_pair = LinkedPair(current.key, current.value)

                    # if there's a collision at that index
                    if new_storage[new_index]:

                        # grab the linked list at that index
                        new_list = new_storage[new_index]

                        # add the linked pair to the end of that list
                        new_list.tail.next = new_pair
                        new_list.tail = new_pair

                    # if no collisions at new index,
                    else:
                         # make a new Ll and store the new pair
                        new_storage[new_index] = LinkedList(new_pair)

                    current = current.next

        self.storage = new_storage

        return self


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
