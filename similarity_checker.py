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

    def check_length(self, word1, word2):
        self.check_validity(word1, word2)

        if len(word1) == len(word2):
            return 60

        score = 60 - (len(word2) - len(word1)) * 60 / len(word1)

        return score
