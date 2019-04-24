from hash_table import HashTable


class Set:

    def __init__(self, elements=None):
        # Initialize a empty hash table
        self.hash_table = HashTable()

        if elements:
            for element in elements:
                if self.contains(element) is False:  # Add the item to the set if it doesn't exist
                    self.add(element)

    def __str__(self):
        """Return a formatted string representation of this set."""
        items = ['({!r})'.format(item) for item in self.hash_table.items()]
        return ''.join(items)

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.hash_table.items())

    def size(self):
        """Return an integer representing the size to the set"""
        return self.hash_table.size

    def contains(self, element):
        """Returning a boolean indicating whether the hash table has the element already"""
        return self.hash_table.contains(element)

    def add(self, element):
        """Add an element to set if its unique"""
        if self.contains(element) is False:
            self.hash_table.set(element, element)

    def remove(self, element):
        """Remove the element from the set, Raise KeyError is not found"""
        if self.hash_table.contains(element):
            self.hash_table.delete(element)
        else:
            raise KeyError('Element not found:'.format(element))
