from redact_problem import redact_words

import unittest


class RedactTest(unittest.TestCase):

    def test_positive(self):
        text_array = 'A brown fox jump over the dog'.split()
        banned_word = ['brown', 'over']

        filter_array = redact_words(text_array, banned_word)

        assert 'brown' not in filter_array
        assert 'over' not in filter_array
        assert len(filter_array) == 5

    def test_upper_case(self):
        text_array = 'A a a jump over the dog'.split()
        banned_word = ['a']

        filter_array = redact_words(text_array, banned_word)
        assert filter_array.count('a') == 0
        assert filter_array.count('A') == 0
        assert len(filter_array) == 4



