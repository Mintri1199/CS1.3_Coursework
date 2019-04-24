from sets import Set
import unittest


class SetTests(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size() == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        duplicate_input_set = Set(['A', 'A', 'C'])
        assert s.size() == 3
        assert duplicate_input_set.size() == 2  # Don't add the duplicate

    def test_contains(self):
        s = Set(['A', 'B', 'C'])
        assert s.contains('A') is True
        assert s.contains('B') is True
        assert s.contains('C') is True
        assert s.contains('D') is False

    def test_add(self):
        s = Set()
        assert s.size() == 0
        s.add('A')
        assert s.size() == 1
        assert s.contains('A') is True

    def test_remove(self):
        s = Set(['A', 'B', 'C'])
        assert s.size() == 3
        s.remove('A')
        assert s.size() == 2
        assert s.contains('A') is False
        with self.assertRaises(KeyError):  # Raise error since D does not exist to remove
            s.remove('D')

    def test_union(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['D', 'A', 'C'])
        union_set = s.union(other_set)
        assert union_set.size() == 4
        assert union_set.contains('A') is True
        assert union_set.contains('B') is True
        assert union_set.contains('C') is True
        assert union_set.contains('D') is True
        assert union_set.contains('E') is False

    def test_intersection(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'C', 'D'])
        inter_set = s.intersection(other_set)
        assert inter_set.size() == 2
        assert inter_set.contains('A') is True
        assert inter_set.contains('C') is True
        assert inter_set.contains('B') is False

    def test_difference(self):
        s = Set(['A', 'B', 'C'])
        other_set = Set(['A', 'C', 'D'])
        diff_set = s.difference(other_set)
        assert diff_set.size() == 2
        assert diff_set.contains('B') is True
        assert diff_set.contains('D') is True
        assert diff_set.contains('A') is False
        assert diff_set.contains('C') is False

