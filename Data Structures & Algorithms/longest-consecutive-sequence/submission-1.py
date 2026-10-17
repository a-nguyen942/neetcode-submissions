class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2, 1, 1, 10, 9, 8, 7 ,3]
        nums_set = set(nums)
        # (2, 1, 10, 9, 8, 7, 3)
        max_longest_consecutive = 0
        for value in nums_set:
            curr_longest_consecutive = 1
            curr = value
            if curr + 1 not in nums_set:
                while((curr - 1) in nums_set):
                    curr -= 1
                    curr_longest_consecutive += 1
                if max_longest_consecutive < curr_longest_consecutive:
                    max_longest_consecutive = curr_longest_consecutive
        return max_longest_consecutive