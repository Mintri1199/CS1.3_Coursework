class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the size of the linked list"""
        return self.size  # O(1)

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        """Maybe I can implement this in a different way"""

        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data

        # Best case running time: O(1) if the index is 0 or the last index of the linked list
        # Worse case running time: O(n) if the index is the second last index

        counter = 0

        if counter == index:  # User inputted 0
            return self.head.data

        elif index == self.size:  # If the user want the last node
            return self.tail.data

        node = self.head

        while counter != index:
            node = node.next
            counter += 1

        return node.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it

        # Best Case: O(1) if index is 0 so the program will call prepend
        # Worse Case: O(n) if the index is the last index of the linked list

        if index == 0:  # If the user want to prepend
            self.prepend(item)
            return

        elif index == self.size:
            self.append(item)
            return

        previous_node = None
        current_node = self.head

        counter = 0

        while counter != index:  # O(n) keep iterating until the counter match the index
            previous_node = current_node  # O(1) reassign the previous node to the current node
            current_node = current_node.next  # O(1) reassign the current node to the next node
            counter += 1

        new_node = Node(item)  # O(1) Instantiate a new node
        new_node.previous = previous_node
        previous_node.next = new_node  # O(1) Change the next pointer of the previous node to the new node
        new_node.next = current_node  # O(1) assign the new node next pointer to the current node
        current_node.previous = new_node
        self.size += 1

    def append(self, item):
        # Best Case: O(1) if the linked list is empty
        # Worse Case: O(1) if the linked list is not empty but there is a tail

        # Create a new node to hold the given item
        new_node = Node(item)  # O(1)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node  # O(1)
        else:
            # Otherwise insert new node after tail while also assign the previous pointer
            self.tail.next = new_node  # O(1)
            new_node.previous = self.tail
        # Update tail to new node regardless
        self.tail = new_node  # O(1)
        # Increment the size by 1
        self.size += 1  # O(1)

    def prepend(self, item):
        """Best Case: O(1)"""
        """Worse Case: O(1)"""

        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node  # O(1)
        else:
            # Otherwise insert new node before head while also assign the previous pointer
            new_node.next = self.head  # O(1)
            self.head.previous = new_node
        # Update head to new node regardless
        self.head = new_node  # O(1)
        # Increment the size by 1
        self.size += 1  # O(1)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object

        # Best case running time: O(1) if the targeted node is at the head or the tail
        # Worse case running time: O(n) if the targeted node is the second last node

        if self.head.data == old_item:
            self.head.data = new_item
            return

        elif self.tail.data == old_item:
            self.tail.data = new_item
            return

        node = self.head

        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return

            else:
                node = node.next

        raise ValueError('old item is not found')

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # n = Number of node in the linked list
        # Best Case: O(1) if the targeted item is at the beginning
        # Worse Case: O(n) if the targeted item is at the end of the linked list

        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:  # O(n)
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                next_node = node.next
                previous.next = next_node
                next_node.previous = previous
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                # Unlink the found node from the next node
                self.head = node.next
                if node.next is not None:
                    self.head.previous = None
                node.next = None

            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node

                    previous.next = None
                # Update tail to the previous node regardless
                node.previous = None
                self.tail = previous

            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_doubly_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    print(ll.head.next)
    print(ll.head.previous)
    ll.append('B')
    print(ll)
    print(ll.tail.next)
    print(ll.tail.previous)
    ll.append('C')
    print(ll)
    print(ll.tail.next)
    print(ll.tail.previous)
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))

    # print('Getting items by index:')
    # for index in range(ll.size):
    #     item = ll.get_at_index(index)
    #     print('get_at_index({}): {!r}'.format(index, item))
    #
    # print('Deleting items:')
    # ll.delete('B')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_doubly_linked_list()

