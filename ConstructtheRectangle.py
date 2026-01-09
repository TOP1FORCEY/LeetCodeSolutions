class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # return is [L, W]. Where L is always bigger then W
        
        w = int(area ** 0.5)
        
        while area % w:           
            w -= 1
        return [area // w, w] 
                
        
area = 6    
    
s = Solution()
print(s.constructRectangle(area))