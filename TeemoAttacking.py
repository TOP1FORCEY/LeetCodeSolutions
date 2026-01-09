class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        
        time = []
        
        for attack in timeSeries:
            time.extend(range(attack, attack + duration))
        
        return len(set(time))
        
duration = 2
timeSeries = [1,2]
 
s = Solution()
print(s.findPoisonedDuration(timeSeries, duration))