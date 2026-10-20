class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_arr = []
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_count += 1
        if zero_count > 1: 
            product_arr = [0] * len(nums)
            return product_arr

        for i in range(len(nums)):
            if zero_count == 0:
                product_arr.append(int(product/nums[i]))
            else:
                if(nums[i]) == 0:
                    product_arr.append(int(product))
                else:
                    product_arr.append(0)


            
        return product_arr