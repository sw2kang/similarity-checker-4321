from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):

    def setUp(self):
        super().setUp()
        self.checker = SimilarityChecker()

    def validity_fail_check(self, args):
        try:
            self.checker.check_length(*args)
            self.fail()
        except TypeError:
            pass

    def validity_pass_check(self, args):
        try:
            self.checker.check_length(*args)
        except:
            self.fail()

    def test_failing_validity(self):
        self.validity_fail_check(('ab', 'cd'))
        self.validity_fail_check(('ab',))
        self.validity_fail_check(('ab', 'cd', 'ef'))
        self.validity_fail_check(('ab', None))
        self.validity_fail_check(('ABC',))
        self.validity_fail_check(('ABC', 'BBC', 'CDE'))

    def test_passing_validity(self):
        self.validity_pass_check(('AB', 'CDEF'))
        self.validity_pass_check(('ABCD', 'A'))

    def test_get_length_similarity(self):
        actual = self.checker.check_length('AB', 'CDEF')
        expected = 0
        self.assertEqual(actual, expected)
