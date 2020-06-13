from unittest import TestCase
import time
from data_structures.arrays.InterviewProblems import is_anagram, is_anagram2, is_anagram3
from data_structures.arrays.InterviewProblems import array_pair_sum
from data_structures.arrays.InterviewProblems import find_missing_sum, find_missing_xor
from data_structures.arrays.InterviewProblems import large_cont_sum
from data_structures.arrays.InterviewProblems import reverse_sentence, reverse_sentence_basic
from data_structures.arrays.InterviewProblems import string_compression
from data_structures.arrays.InterviewProblems import unique_char_in_str, unique_char_in_str2


class TestInterviewProblems(TestCase):
    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(' ({:.5})'.format(elapsed), end=" ")

    def test_anagram(self):
        self.assertTrue(is_anagram('dog', 'god'))
        self.assertTrue(is_anagram('clint eastwood', 'old west action'))
        self.assertTrue(is_anagram('go go go', 'gggooo'))
        self.assertTrue(is_anagram('abc', 'cba'))
        self.assertTrue(is_anagram('hi man', 'hi     man'))

        self.assertFalse(is_anagram('aabbcc', 'aabbc'))
        self.assertFalse(is_anagram('123', '1 2'))
        self.assertFalse(is_anagram('aa', 'bb'))

    def test_anagram2(self):
        self.assertTrue(is_anagram2('dog', 'god'))
        self.assertTrue(is_anagram2('clint eastwood', 'old west action'))
        self.assertTrue(is_anagram2('go go go', 'gggooo'))
        self.assertTrue(is_anagram2('abc', 'cba'))
        self.assertTrue(is_anagram2('hi man', 'hi     man'))

        self.assertFalse(is_anagram2('aabbcc', 'aabbc'))
        self.assertFalse(is_anagram2('123', '1 2'))
        self.assertFalse(is_anagram2('aa', 'bb'))

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

    def test_find_missing_sum(self):
        self.assertEqual(find_missing_sum([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(find_missing_sum([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(find_missing_sum([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        self.assertEqual(find_missing_sum(range(100000), range(99999)), 99999)

    def test_find_missing_xor(self):
        self.assertEqual(find_missing_xor([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(find_missing_xor([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(find_missing_xor([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        self.assertEqual(find_missing_sum(range(100000), range(99999)), 99999)

    def test_large_cont_sum(self):
        self.assertEqual(large_cont_sum([1, 2, -1, 3, 4, -1]), (9, 1, 4))
        self.assertEqual(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]), (29, 1, 10))
        self.assertEqual(large_cont_sum([-1, 1]), (1, 1, 1))

    def test_reverse_sentence(self):
        self.assertEqual(reverse_sentence('    space before'), 'before space')
        self.assertEqual(reverse_sentence('space after     '), 'after space')
        self.assertEqual(reverse_sentence('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(reverse_sentence('1'), '1')

    def test_reverse_sentence(self):
        self.assertEqual(reverse_sentence_basic('    space before'), 'before space')
        self.assertEqual(reverse_sentence_basic('space after     '), 'after space')
        self.assertEqual(reverse_sentence_basic('   Hello John    how are you   '), 'you are how John Hello')
        self.assertEqual(reverse_sentence_basic('1'), '1')

    def test_string_compression(self):
        self.assertEqual(string_compression(''), '')
        self.assertEqual(string_compression('AABBCC'), 'A2B2C2')
        self.assertEqual(string_compression('AAABCCDDDDD'), 'A3B1C2D5')

    def test_unique_char_in_str(self):
        self.assertEqual(unique_char_in_str(''), True)
        self.assertEqual(unique_char_in_str('goo'), False)
        self.assertEqual(unique_char_in_str('abcdefg'), True)

    def test_unique_char_in_str2(self):
        self.assertEqual(unique_char_in_str2(''), True)
        self.assertEqual(unique_char_in_str2('goo'), False)
        self.assertEqual(unique_char_in_str2('abcdefg'), True)
