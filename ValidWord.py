class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowels = set("aeiouAEIOU")
        letters = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        letters_only = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        if len(word) < 3:
            return False
        
        for letter in word:
            if letter not in letters:
                return False

        if not any(ch in vowels for ch in word):
            return False

        consonants = letters_only - vowels

        if not any(ch in consonants for ch in word):
            return False
        
        return True
        

word = "234Adas"

s = Solution()
print(s.isValid(word))