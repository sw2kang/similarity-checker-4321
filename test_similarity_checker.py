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

    def length_score_check(self, args, expected_score):
        actual_score = self.checker.check_length(*args)
        self.assertEqual(expected_score, actual_score)

    def test_failing_validity(self):
        self.validity_fail_check(('ab', 'cd'))
        self.validity_fail_check(('ab',))
        self.validity_fail_check(('ab', 'cd', 'ef'))
        self.validity_fail_check(('ab', None))
        self.validity_fail_check(('ABC',))
        self.validity_fail_check(('ABC', 'BBC', 'CDE'))
        self.validity_fail_check(('', ''))
        self.validity_fail_check(('ABC', ''))

    def test_passing_validity(self):
        self.validity_pass_check(('AB', 'CDEF'))
        self.validity_pass_check(('ABCD', 'A'))

    def test_get_length_similarity(self):
        self.length_score_check(('AB', 'CDEF'), 0)
        self.length_score_check(('ABCD', 'CDEF'), 60)
