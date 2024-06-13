from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test_validity(self):
        try:
            checker = SimilarityChecker()
            checker.check_length('ab', 'cd')
            self.fail()
        except TypeError:
            pass
