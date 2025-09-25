class Solution(object):
    def maxArea(self, height = list):
        """
        :type height: List[int]
        :rtype: int
        """
        volume = []
        
        if len(height) == 2:
            return min(height)
        
        for p, h in enumerate(height):            
            for p2, h2 in enumerate(height):
                print(p, h," ", p2, h2," ", h * (p2 - 1))
                if (p2 - p) > 0:
                    volume.append(min(h, h2) * (p2 - p))
            
        print(volume)
        return max(volume)
        
        
num = [1,8,6,2,5,4,8,3,7]

s = Solution()
print(s.maxArea(num))