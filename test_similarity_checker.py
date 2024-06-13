from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):

    def setUp(self):
        super().setUp()
        self.checker = SimilarityChecker()

    def test_failing_validity(self):
        try:
            self.checker.check_length('ab', 'cd')
            self.fail()
        except TypeError:
            pass

        try:
            self.checker.check_length('ab', 'cd', 'ef')
            self.fail()
        except TypeError:
            pass

        try:
            self.checker.check_length('ab')
            self.fail()
        except TypeError:
            pass

        try:
            self.checker.check_length('ab', None)
            self.fail()
        except TypeError:
            pass

    def test_passing_validity(self):
        try:
            self.checker.check_length('AB', 'CDEF')
        except:
            self.fail()
