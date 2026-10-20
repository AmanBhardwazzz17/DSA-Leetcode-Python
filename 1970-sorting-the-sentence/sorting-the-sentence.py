class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  # Sentence ko words mein divide karo
        result = [""] * len(words)  # Empty positions banao
        for word in words:
            num = int(word[-1])  # Position number nikalo
            clean_word = word[:-1]  # Last digit hatao
            result[num - 1] = clean_word  # Correct position par rakho
        return " ".join(result)  # Words ko sentence mein jodo