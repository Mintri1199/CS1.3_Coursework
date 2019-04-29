#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefpytABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
    # Check if the characters in the string is valid with the base
    # if any(c not in string.printable[: base] for c in digits):  # Generator expression
    #     print('Invalid characters for base: {}'.format(base))
    #     return

    # TODO: Decode digits from binary (base 2)
    result = 0.0
    # digits = digits[::-1]  # Reassign the digits string in reverse order

    # if base == 2:  # The base is 2
    #     digits = digits[::-1]  # Reassign the digits in reverse order and convert it to integer
    #     for i in range(len(digits)):
    #         current_bit = int(digits[i])
    #         if current_bit == 1:
    #             result += 2**i
    #
    #     return result
    #
    # # TODO: Decode digits from hexadecimal (base 16)
    # if base == 16:
    #     digits = digits[::-1]
    #     for power in range(len(digits)):
    #         power_value = 16**power
    #         char = digits[power]  # Assign the character of the specific power
    #         numerical_value = string.hexdigits.find(char)  # Find the numerical value of the character
    #         product = power_value * numerical_value
    #         result += product
    #
    #     return result

    # TODO: Decode digits from any base (2 up to 36)
    # for power_index in range(len(digits)):
    #     power_value = base**power_index  # The result of the base in the power of the power index
    #     char = digits[power_index]  # Get the character of the digits string using the power index
    #     numerical_value = string.printable.find(char)  # Get the numerical value of the selected character
    #     result += power_value * numerical_value  # Increment result with the product of (base**power)*numerical value
    #
    #
    # power = 0
    if "." in digits:
        radix_index = digits.index(".")
        power = len(digits[:radix_index]) - 1
    else:
        power = len(digits) - 1

    for character in digits:
        if character == '.':
            pass
        else:
            char_index = string.printable.index(character)
            result += (base ** power) * char_index
            power -= 1

    return result

#
#
# def encode(number, base):
#     """Encode given number in base 10 to digits in given base.
#     number: int -- integer representation of number (in base 10)
#     base: int -- base to convert to
#     return: str -- string representation of number (in given base)"""
#     # Handle up to base 36 [0-9a-z]
#     assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
#     # Handle unsigned numbers only for now
#     assert number >= 0, 'number is negative: {}'.format(number)
#     if number == 0:
#         return "0"
#
#     encode_str = ''
#     current_power = 0
#     finished = False
#     list_of_powers = []
#     string_number = str(number)
#     whole = int(number)
#     fraction = number - whole
#
#     while finished is False:  # Get all the possible power of a base for the number
#         power_value = base**current_power
#         if power_value < whole:
#             list_of_powers.insert(0, current_power)
#             current_power += 1
#
#         elif power_value == whole:
#             list_of_powers.insert(0, current_power)
#             finished = True
#
#         else:  # The current power made the base too big
#             finished = True
#
#     for power in list_of_powers:
#         power_value = base ** power
#         limit = int(whole / power_value)
#         whole -= power_value * limit
#
#         encode_str += string.printable[limit]
#
#     return encode_str


# TODO: Add Comments and annotate complexity this file
# Encoding function from Zurich Okoren after bugs fixed by me
def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    result = ''
    integral = int(number)
    fractional = number - integral
    print(number - integral)
    while integral > 0:
        div_tup = divmod(integral, base)   # Return a tuple of (quotient, remainder)
        integral = div_tup[0]
        result = str(string.printable[div_tup[1]]) + result

    if fractional:
        result += '.'
        print("Initial fraction: {}".format(fractional))
        while fractional != 0:
            fractional *= base
            fract_bit = int(fractional)
            print(fractional)
            print(fract_bit)
            if fract_bit != 0:
                result += string.printable[fract_bit]
            else:
                result += '0'
            fractional -= fract_bit

    return result


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Check if the digits has any invalid character for base 1
    # if any(c not in string.printable[: base1] for c in digits):  # Generator expression
    #     print('Invalid characters for base1: {}'.format(base1))
    #     return

    number = decode(digits, base1)
    converted_str = encode(number, base2)

    return converted_str


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


if __name__ == '__main__':
    main()

print(decode('10110.101', 2))
# print(encode(134.34, 16))
