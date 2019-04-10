def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # cheating way
    # return pattern in text

    if len(pattern) == 0:
        return True

    current_index = 0  # Keep track of the current character of the pattern

    for char in text:

        if char == pattern[current_index]:
            # increment the current index
            current_index += 1

            if current_index >= len(pattern):  # The pattern has been found
                return True
        else:
            current_index = 0  # Reset the current index
            if char == pattern[current_index]:  # check if the current character still match the first char of pattern
                current_index += 1

    return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    found_index = None
    current_index = 0

    if pattern == '':
        return 0

    for index, char in enumerate(text):
        if char == pattern[current_index]:
            if found_index == None:
                found_index = index

            current_index += 1

            if current_index >= len(pattern):
                return found_index
        else:
            current_index = 0
            found_index = None
            if char == pattern[current_index]:
                found_index = index
                current_index += 1


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")

#
# if __name__ == '__main__':
#     main()

# print(contains('ababc', 'abc'))

print(find_index('ababc', 'abc'))
