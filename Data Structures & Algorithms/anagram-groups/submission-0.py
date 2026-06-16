class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            letter_freq = [0] * 26
            for c in s:
                letter_freq[ord(c) - ord('a')] += 1
            letter_freq = tuple(letter_freq)
            if letter_freq in anagram_dict:
                anagram_dict[letter_freq].append(s)
            else:
                anagram_dict[letter_freq] = [s]
        result = []
        for key in anagram_dict:
            result.append(anagram_dict[key])
        return result