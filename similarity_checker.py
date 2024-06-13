class SimilarityChecker:
    def check_length(self, word1, word2):
        for c in word1:
            if not ord('A') <= ord(c) <= ord('Z'):
                raise TypeError()

        for c in word2:
            if not ord('A') <= ord(c) <= ord('Z'):
                raise TypeError()

        if len(word1) == 0 or len(word2) == 0:
            raise TypeError()

        if len(word1) == len(word2):
            return 60

        return 0

