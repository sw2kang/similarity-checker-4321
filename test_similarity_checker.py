from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarityChecker()

    def count_validity_fail_check(self, args):
        try:
            self.checker.check_count(*args)
            self.fail()
        except TypeError:
            pass

    def count_validity_pass_check(self, args):
        try:
            self.checker.check_count(*args)
        except:
            self.fail()

    def count_score_check(self, args, expected_score):
        actual_score = self.checker.check_count(*args)
        self.assertEqual(expected_score, actual_score)

    def test_count_failing_validity(self):
        self.count_validity_fail_check(('ab', 'cd'))
        self.count_validity_fail_check(('ab',))
        self.count_validity_fail_check(('ab', 'cd', 'ef'))
        self.count_validity_fail_check(('ab', None))
        self.count_validity_fail_check(('ABC',))
        self.count_validity_fail_check(('ABC', 'BBC', 'CDE'))
        self.count_validity_fail_check(('', ''))
        self.count_validity_fail_check(('ABC', ''))

    def test_count_passing_validity(self):
        self.count_validity_pass_check(('AB', 'CDEF'))
        self.count_validity_pass_check(('ABCD', 'A'))

    def test_get_length_similarity(self):
        self.count_score_check(('ASD', 'DSA'), 40)
        self.count_score_check(('A', 'BB'), 0)
        self.count_score_check(('AAAAAB', 'BBA'), 40)
        self.count_score_check(('AA', 'AAE'), 20)
