from linkedlist import LinkedList


class LinkedListDeque:

    def __init__(self, iterable=None):
        # Initialize a new Doubly linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={}, last={}'.format(self.length(), self.peek_first(), self.peek_last())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def append(self, item):
        """ Insert the given item to the end of the double ended queue"""
        self.list.append(item)

    def prepend(self, item):
        """ Insert the given item to the end of the double ended queue"""
        self.list.prepend(item)

    def peek_first(self):
        """Return the item on the top of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        else:
            return self.list.head.data

    def peek_last(self):
        """Return the item on the end of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        else:
            return self.list.tail.data

    def pop_first(self):
        """Remove and return the item on the top of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – Since the targeted node is the head of the linked list"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            top_value = self.list.head.data
            self.list.delete(top_value)
            return top_value

    def pop_last(self):
        """Remove and return the item on the end of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Since the program have to traverse through the Linked list to get the second last node"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            top_value = self.list.tail.data
            self.list.delete(top_value)
            return top_value
