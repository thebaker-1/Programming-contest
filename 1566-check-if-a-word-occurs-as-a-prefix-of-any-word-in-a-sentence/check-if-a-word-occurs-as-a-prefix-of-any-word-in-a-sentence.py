class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = list(((sentence.split(" "))))
        word_len = len(searchWord)
        for i in range(len(words)):
            if len(words[i])>=word_len and searchWord == words[i][:word_len]:
                return i+1

        return -1
        