class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")        
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        output = []
        
        for word in words:
            if set(word.lower()) <= row1 or set(word.lower()) <= row2 or set(word.lower()) <= row3:
                output.append(word)
                
        return output

words = ["Hello","Alaska","Dad","Peace"]

s = Solution()
print(s.findWords(words))