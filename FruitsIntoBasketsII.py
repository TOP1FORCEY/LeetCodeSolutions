class Solution(object):
    def numOfUnplacedFruits(self, fruits = list, baskets = list):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        
        while fruits and baskets:
            for fruit in fruits[:]:           # iterate over a copy
                for basket in baskets:
                    if fruit <= basket:
                        fruits.remove(fruit)  
                        baskets.remove(basket)
                        print(fruit, basket)
                        break
                else:
                    continue
                
            if fruits and baskets and fruits[0] > baskets[0]:
                return len(fruits)

        return len(fruits)


fruits = [4,2,5]
baskets = [3,5,4]

s = Solution()
print(s.numOfUnplacedFruits(fruits, baskets))