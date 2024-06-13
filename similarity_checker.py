class SimilarityChecker:
    def check_length(self, word1, word2):
        for c in word1:
            if not ord('A') <= ord(c) <= ord('Z'):
                raise TypeError()

        for c in word2:
            if not ord('A') <= ord(c) <= ord('Z'):
                raise TypeError()

