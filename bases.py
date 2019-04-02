#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
string.digits is '0123456789'
string.hexdigits is '0123456789abcdefABCDEF'
string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    # assert int(digits) is int
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    if base == 2:  # The base is 2
        digits = digits[::-1]  # Reassign the digits in reverse order and convert it to integer
        result = 0
        for i in range(len(digits)):
            current_bit = int(digits[i])
            if current_bit == 1:
                result += 2**i

        return result

    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    if base == 2:
        binary_str = ''
        current_power = 0
        power_array = []
        not_finished = True

        while not_finished:
            bit_value = 2**current_power
            if bit_value < number:  # Current power is less than the number
                power_array.insert(0, current_power)
                current_power += 1

            elif bit_value == number:  # Current power is equal to the number
                power_array.insert(0, current_power)
                not_finished = False

            else:  # The current power is more than the number
                not_finished = False

        for power in power_array:
            value = 2**power
            if value <= number:
                number -= value
                binary_str += "1"

            else:  # bit_value is greater than number
                binary_str += "0"

        return binary_str

    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

print(encode(698, 2))

# print(decode('101101', 2))

# if __name__ == '__main__':
#     main()
