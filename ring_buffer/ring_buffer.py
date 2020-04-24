from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if the buffer is full, compare lenght of storage to self.capacity
        if len(self.storage) == self.capacity:
            # if full, replace oldest item with new item
            pass
        else:
            # add new item to the tail
            self.storage.add_to_tail(item)
            # set current to tail, the item just added
            self.current = self.storage.tail
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
