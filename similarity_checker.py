MAX_COUNT_SCORE = 40


class SimilarityChecker:
    def check_validity(self, word1, word2):
        for c in word1:
            if not ord('A') <= ord(c) <= ord('Z'):
                raise TypeError()
        for c in word2:
            if not ord('A') <= ord(c) <= ord('Z'):
                raise TypeError()
        if len(word1) == 0 or len(word2) == 0:
            raise TypeError()

    def get_count_score(self, word1, word2):
        same_count = len(set(word1) & set(word2))
        total_count = len(set(word1) | set(word2))
        score = same_count * MAX_COUNT_SCORE / total_count
        return score

    def check_count(self, word1, word2):
        self.check_validity(word1, word2)

        score = self.get_count_score(word1, word2)

        return score
