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
        """Return an integer representing the size to the set
           Time Complexity: O(1) because the alternate length method in the hash table"""

        return self.hash_table.size

    def contains(self, element):
        """Returning a boolean indicating whether the hash table has the element already
           Time Complexity: O(L) where L is the number of item in the indexed bucket"""
        return self.hash_table.contains(element)

    def add(self, element):
        """Add an element to set if its unique
           Time Complexity: O(l) where L is the number of item in the indexed bucket"""

        if self.contains(element) is False:  # O(L)
            self.hash_table.set(element, None)  # O(L)

    def remove(self, element):
        """Remove the element from the set, Raise KeyError is not found
           Time Complexity: O(l) where L is the number of item in the indexed bucket"""

        if self.hash_table.contains(element):  # O(L)
            self.hash_table.delete(element)  # O(L)
        else:
            raise KeyError('Element not found:'.format(element))

    def union(self, other_set):
        """Assuming the input is a Set object, use iterable to make union easier
           Return a new set that is a union of this set and other set
           Time Complexity: O(n + m) -> O(n) because it is O(n) to create a new set
           and O(m) for add elements from other set"""
        union_set = Set(self.hash_table.keys())  # O(n) where n is the number of elements in the set
        # Initialize a new set that has all the elements from itself

        for item in other_set:  # O(m) where m is the number of elements in the other set
            union_set.add(item)  # O(L)

        return union_set

    def intersection(self, other_set):
        """Assuming the input is a Set object, use iterable to make intersection easier
           Return a new set that only contains the common elements between two sets
           Time Complexity: O(n) because it has to compare all elements from both sets to find common elements"""
        intersection_set = Set()  # Initialize a new empty set  O(1)

        # Determining which sets is bigger
        if other_set.size() >= self.size():  # O(1)
            bigger_set = other_set  # O(1)
            smaller_set = self  # O(1)

        else:
            bigger_set = self  # O(1)
            smaller_set = other_set  # O(1)

        for item in smaller_set:  # item = key
            if bigger_set.contains(item):  # O(L)
                intersection_set.add(item)  # O(L)

        return intersection_set

    def difference(self, other_set):
        """Assuming the input is a Set object, use iterable to make difference easier
           Return a new set that only contains the difference elements between two sets
           Time Complexity: O(n + m) -> O(n) because it is O(n) to create a new set
           and O(m) for add elements from other set
            TODO: How can I improve this? """
        difference_set = Set()  # Initialize a new empty set O(1)

        # Formula: union - intersection = difference
        union_set = self.union(other_set)  # O(n)
        inter_set = self.intersection(other_set)  # O(n)

        # This is not efficient
        for element in union_set:  # O(n)
            if inter_set.contains(element) is False:  # O(L)
                difference_set.add(element)  # O(L)

        return difference_set

    def is_subset(self, other_set):
        """Assuming the input is a Set object, use iterable to make is_subset easier
           Return a boolean indicate whether the base has all the elements of the other set
           Time Complexity: O(n) where n is the number of elements in the other set"""

        # Making sure the other set is smaller than the base set
        if other_set.size() > self.size():  # O(1)
            return False

        if other_set.size() == 0:  # O(1)
            return True

        counter = 0

        for element in other_set:  # O(n)
            if self.contains(element):  # O(L)
                counter += 1

        return counter == other_set.size()  # O(1)
