#
# https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
#

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1

        result = [1] * len(nums)

        for i in range(len(nums)-1):
            result[i+1] = pre * nums[i]
            pre = pre * nums[i]
        
        for j in range(len(nums)-1, 0, -1):
            result[j-1] = post * nums[j]  * result[j-1]
            post = post * nums[j]
        
        return result
