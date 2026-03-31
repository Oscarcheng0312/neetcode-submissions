class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # the key is the number, and value is its frequency
        # store all the element into the map
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # use a min heap then pop k element
        min_heap = []
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [pair[1] for pair in min_heap]

        
