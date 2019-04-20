from double_ended_queue import Deque
import unittest


class DequeTest(unittest.TestCase):

    def test_init(self):
        s = Deque()
        assert s.peek_first() is None
        assert s.peek_last() is None
        assert s.length() == 0
        assert s.is_empty() is True

    def test_init_with_list(self):
        s = Deque(['A', 'B', 'C'])
        assert s.peek_last() == 'C'
        assert s.peek_first() == 'A'
        assert s.length() == 3
        assert s.is_empty() is False

    def test_length(self):
        s = Deque()
        assert s.length() == 0
        s.append('A')
        assert s.length() == 1
        s.append('B')
        assert s.length() == 2
        s.pop_last()
        assert s.length() == 1
        s.pop_last()
        assert s.length() == 0

    def test_append(self):
        s = Deque()
        s.append('A')
        assert s.peek_first() == 'A'
        assert s.peek_last() == 'A'
        assert s.length() == 1
        s.append('B')
        assert s.peek_last() == 'B'
        assert s.length() == 2
        s.append('C')
        assert s.peek_last() == 'C'
        assert s.length() == 3
        assert s.is_empty() is False

    def test_prepend(self):
        s = Deque()
        s.prepend('A')
        assert s.peek_first() == 'A'
        assert s.peek_first() == 'A'
        assert s.length() == 1
        s.prepend('B')
        assert s.peek_first() == 'B'
        assert s.length() == 2
        s.prepend('C')
        assert s.peek_first() == 'C'
        assert s.length() == 3
        assert s.is_empty() is False

    def test_peek_first(self):
        s = Deque()
        assert s.peek_first() is None
        s.append('A')
        assert s.peek_first() == 'A'
        s.append('B')
        assert s.peek_first() == 'A'
        s.pop_last()
        assert s.peek_first() == 'A'
        s.pop_last()
        assert s.peek_first() is None

    def test_peek_last(self):
        s = Deque()
        assert s.peek_last() is None
        s.append('A')
        assert s.peek_last() == 'A'
        s.append('B')
        assert s.peek_last() == 'B'
        s.pop_last()
        assert s.peek_last() == 'A'
        s.pop_last()
        assert s.peek_last() is None

    def test_pop_last(self):
        s = Deque(['A', 'B', 'C'])
        assert s.pop_last() == 'C'
        assert s.length() == 2
        assert s.pop_last() == 'B'
        assert s.length() == 1
        assert s.pop_last() == 'A'
        assert s.length() == 0
        assert s.is_empty() is True
        with self.assertRaises(ValueError):
            s.pop_last()

    def test_pop_first(self):
        s = Deque(['A', 'B', 'C'])
        assert s.pop_first() == 'A'
        assert s.length() == 2
        assert s.pop_first() == 'B'
        assert s.length() == 1
        assert s.pop_first() == 'C'
        assert s.length() == 0
        assert s.is_empty() is True
        with self.assertRaises(ValueError):
            s.pop_first()


if __name__ == '__main__':
    unittest.main()
