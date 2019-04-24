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
        items = ['({!r})'.format(item) for item in self.hash_table.keys()]
        return ''.join(items)

    def __iter__(self):
        """Make the set iterable and return the keys of the items"""
        for item in self.hash_table.keys():
            yield item

    def __repr__(self):
        """Return a string representation of this linked list."""
        return '({!r})'.format(self.hash_table.keys())

    def size(self):
        """Return an integer representing the size to the set"""
        return self.hash_table.size

    def contains(self, element):
        """Returning a boolean indicating whether the hash table has the element already"""
        return self.hash_table.contains(element)

    def add(self, element):
        """Add an element to set if its unique"""
        if self.contains(element) is False:
            self.hash_table.set(element, None)

    def remove(self, element):
        """Remove the element from the set, Raise KeyError is not found"""
        if self.hash_table.contains(element):
            self.hash_table.delete(element)
        else:
            raise KeyError('Element not found:'.format(element))

    def union(self, other_set):
        """Assuming the input is a Set object, use iterable to make union easier
        Return a new set that is a union of this set and other set"""
        union_set = Set(self.hash_table.keys())  # Initialize a new set that has all the elements from itself

        for item in other_set:  # item = key
            union_set.add(item)

        return union_set

