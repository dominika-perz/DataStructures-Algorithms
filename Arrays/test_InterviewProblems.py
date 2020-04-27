import unittest
from unittest import TestCase
from timeit import timeit
from Arrays.InterviewProblems import is_anagram, is_anagram2, is_anagram3
from Arrays.InterviewProblems import array_pair_sum
import timeit


class TestInterviewProblems(TestCase):
    def setUp(self):
        self._started_at = timeit.timeit()

    def tearDown(self):
        elapsed = timeit.timeit() - self._started_at
        print(' ({:.5})'.format(elapsed), end=" ")

    @unittest.skip('Anagram done')
    def test_anagram(self):
        self.assertTrue(is_anagram('dog', 'god'))
        self.assertTrue(is_anagram('clint eastwood', 'old west action'))
        self.assertTrue(is_anagram('go go go', 'gggooo'))
        self.assertTrue(is_anagram('abc', 'cba'))
        self.assertTrue(is_anagram('hi man', 'hi     man'))

        self.assertFalse(is_anagram('aabbcc', 'aabbc'))
        self.assertFalse(is_anagram('123', '1 2'))
        self.assertFalse(is_anagram('aa', 'bb'))

    @unittest.skip('Anagram done')
    def test_anagram2(self):
        self.assertTrue(is_anagram2('dog', 'god'))
        self.assertTrue(is_anagram2('clint eastwood', 'old west action'))
        self.assertTrue(is_anagram2('go go go', 'gggooo'))
        self.assertTrue(is_anagram2('abc', 'cba'))
        self.assertTrue(is_anagram2('hi man', 'hi     man'))

        self.assertFalse(is_anagram2('aabbcc', 'aabbc'))
        self.assertFalse(is_anagram2('123', '1 2'))
        self.assertFalse(is_anagram2('aa', 'bb'))

    @unittest.skip('Anagram done')
    def test_anagram3(self):
        self.assertTrue(is_anagram3('dog', 'god'))
        self.assertTrue(is_anagram3('clint eastwood', 'old west action'))
        self.assertTrue(is_anagram3('go go go', 'gggooo'))
        self.assertTrue(is_anagram3('abc', 'cba'))
        self.assertTrue(is_anagram3('hi man', 'hi     man'))

        self.assertFalse(is_anagram3('aabbcc', 'aabbc'))
        self.assertFalse(is_anagram3('123', '1 2'))
        self.assertFalse(is_anagram3('aa', 'bb'))

    def test_array_pair_sum(self):
        self.assertEqual(array_pair_sum([1, 3, 2, 2], 4), 2)
        self.assertEqual(array_pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        self.assertEqual(array_pair_sum([1, 2, 3, 1], 3), 1)
        self.assertEqual(array_pair_sum([1, 3, 2, 2], 4), 2)
