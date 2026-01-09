class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = []
        mag = []
        
        for s in ransomNote:
            note.append(s)
        
        for s in magazine:
            mag.append(s)
                
        for s in note:
            try:
                mag.remove(s)
            except:
                return False
            
        return True
        
        
ransomNote = "aa"
magazine = "aab"

s = Solution()
print(s.canConstruct(ransomNote, magazine))