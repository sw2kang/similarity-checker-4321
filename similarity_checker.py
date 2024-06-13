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

    def check_count(self, word1, word2):
        self.check_validity(word1, word2)
