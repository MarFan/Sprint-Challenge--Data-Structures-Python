from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        if self.storage.length == self.capacity:
            self.current.value = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)                
            current = current.next

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
