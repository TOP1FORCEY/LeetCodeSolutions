class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lenght = len(s.replace("-",""))
        rs = s[::-1].replace("-","")
        
        adj = 0
        
        for space in range(0 + k,lenght,k):
            rs = rs[:space + adj] + "-" + rs[space + adj:]
            adj += 1
            
        return rs[::-1].upper()
        
st = "2-5g-3-J"
k = 2

s = Solution()
print(s.licenseKeyFormatting(st, k))