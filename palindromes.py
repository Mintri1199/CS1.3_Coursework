import string


# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Pseudocode

    # loop until the left and right indexes are the same or cross
    #     check if two characters of the left and right indexes are the same
    #     if not return return False
    #     if yes
    #           increment left index
    #           decrement right index

    # Return True if the text has only one character or zero character

    assert type(text) == str, 'Incorrect input'

    if len(text) == 0 or len(text) == 1:
        return True

    # table = str.maketrans(dict.fromkeys(string.punctuation))  O(p) time and space
    #
    # text = text.translate(table).replace(' ', '').lower()   O(n)  O(n)
    #
    # left_index = 0  O(1)
    # right_index = len(text) - 1  O(1)
    #
    # while right_index >= left_index:
    #     left_character = text[left_index]     O(1)
    #     right_character = text[right_index]   O(1)
    #
    #     if left_character != right_character:
    #         return False
    #
    #     left_index += 1    O(1)
    #     right_index -= 1   O(1)
    #
    # return True
    right_index = len(text) - 1  # O(1)
    left_index = 0  # O(1)

    while left_index < right_index:  # n/2 ==
        # Move the left index over right if the character is not a letter

        if validation(text, left_index, right_index):  # O(1)
            return True

        while text[left_index] not in string.ascii_letters:  # O(n)
            left_index += 1  # O(1)

            if validation(text, left_index, right_index):  # O(1)
                return True

        # Move the right index over left if the character is not a letter
        while text[right_index] not in string.ascii_letters:  # O(n)
            right_index -= 1  # O(1)

            if validation(text, left_index, right_index):  # O(1)
                return True

        if text[left_index].lower() != text[right_index].lower():  # O(1)
            return False

        left_index += 1  # O(1)
        right_index -= 1  # O(1)

    return True


def validation(text, left, right):
    if text[left] not in string.ascii_letters and text[right] not in string.ascii_letters:
        if left + 1 >= right:
            return True
        else:
            return False


def is_palindrome_recursive(text, left=None, right=None):
    # same logic above but instead of reformat the string at the beginning
    # have it move the indexes if the character is not a letter

    if len(text) == 0 or len(text) == 1:
        return True

    # Assign the left and right once
    if left is None and right is None:
        left = 0
        right = len(text) - 1

    # Keep moving the left index to the right until the character is a letter
    while text[left] not in string.ascii_letters:
        left += 1

        #  Check if all the character in the text is non letter character
        #  Check if only one character in the text is a letter
        if validation(text, left, right):
            return True

    # Keeping moving the right to the left until the character is a letter
    while text[right] not in string.ascii_letters:
        right -= 1

        #  Check if all the character in the text is non letter character
        #  Check if only one character in the text is a letter
        if validation(text, left, right):
            return True

    if right >= left:
        if text[left] == text[right]:
            return is_palindrome_recursive(text, left + 1, right - 1)

        elif text[left].lower() == text[right].lower():
            return is_palindrome_recursive(text, left + 1, right - 1)

        else:
            return False

    else:
        return True


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()

print(is_palindrome("!@#$%^&"))