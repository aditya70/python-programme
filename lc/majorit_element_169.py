class Solution:
    def majorityElement(self, nums) -> int:
        # print(str(nums))
        num_set = set(nums)
        # print(str(num_set))
        for x in num_set:
            if nums.count(x) > len(nums)/2:
                return x

s = Solution()
ans=s.majorityElement([1,6,6,6,1,6]) 
print(ans)     