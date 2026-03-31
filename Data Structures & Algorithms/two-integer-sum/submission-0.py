class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return []

        prev_map = {} # the key is element after substaraction, the value is the index of 
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            else:
                prev_map[num] = i

        return []