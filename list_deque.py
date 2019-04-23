class Deque:

    def __init__(self, iterable=None):
        # Initialize a new Doubly linked list to store the items
        self.list = list()
        if iterable is not None:
            self.list.extend(iterable)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={}, last={}'.format(self.length(), self.peek_first(), self.peek_last())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def append(self, item):
        """ Insert the given item to the end of the double ended queue"""
        self.list.append(item)

    def prepend(self, item):
        """ Insert the given item to the end of the double ended queue"""
        self.list.insert(0, item)

    def peek_first(self):
        """Return the item on the top of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        else:
            return self.list[0]

    def peek_last(self):
        """Return the item on the end of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        else:
            return self.list[-1]

    def pop_first(self):
        """Remove and return the item on the top of this queue,
        or raise ValueError if this queue is empty."""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.list.pop(0)

    def pop_last(self):
        """Remove and return the item on the end of this queue,
        or raise ValueError if this queue is empty."""
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.list.pop(-1)
