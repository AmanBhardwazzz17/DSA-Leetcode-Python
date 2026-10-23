class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq = {}
        max_frequency = 0
        max_length = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            current_freq = freq[s[right]]
            max_frequency = max(max_frequency, current_freq)
            window_length = right - left + 1
            required_replacements = window_length - max_frequency
            while required_replacements > k:
                freq[s[left]] -= 1
                left += 1
                window_length = right - left + 1
                required_replacements = window_length - max_frequency
            max_length = max(max_length, window_length)
            right += 1
        return max_length