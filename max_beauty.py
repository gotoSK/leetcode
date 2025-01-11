from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        prices = []
        beauties = []
        answer = []

        items.sort()

        # pre-comupte max beauty for each price
        max_beauty = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            prices.append(price)
            beauties.append(max_beauty)
        
        # find the max beauty corresponding to queries[j]
        for j in queries:
            idx = bisect_right(prices, j) - 1
            if idx >= 0:
                answer.append(beauties[idx])
            else:
                answer.append(0)
        
        return answer
        

# Example usage (for testing/debugging purposes):
if __name__ == "__main__":
    items = [[1, 2], [3, 4], [5, 6]]
    queries = [4, 6]
    
    solution = Solution()
    print(solution.maximumBeauty(items, queries))
