class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution_arr = []
        freq_counter = dict()
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]

        for i in range(len(nums)):
            if nums[i] not in freq_counter:
                freq_counter[nums[i]] = 1
            else:
                freq_counter[nums[i]] += 1

        for key, value in freq_counter.items():
            bucket[value].append(key)
        
        i = n
        while len(solution_arr) < k:
            solution_arr.extend(bucket[i])
            i -= 1
        return solution_arr