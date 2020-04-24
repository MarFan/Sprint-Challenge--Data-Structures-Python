from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        print(self.storage.length)
        
        if not self.current:
            self.storage.add_to_head(item)
            self.current = item
            return

        if self.current == self.storage.tail:
            print(item)
            self.storage.add_to_tail(item)
            return 

        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        pass

    def append(self, item):
        pass

    def get(self):
        pass
