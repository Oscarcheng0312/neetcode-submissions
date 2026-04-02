class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1

        return left
