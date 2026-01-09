class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        places = [0] * len(score)
        place = 1
        
        while place <= len(score):
            s = score.index(max(score))
            
            if place == 1:
                places[s] = "Gold Medal"
            elif place == 2:
                places[s] = "Silver Medal"
            elif place == 3:
                places[s] = "Bronze Medal"
            else:
                places[s] = str(place)
            
            score[s] = -1
            place += 1
            
        return places
            
score = [10,3,8,9,4]
    
s = Solution()
print(s.findRelativeRanks(score))