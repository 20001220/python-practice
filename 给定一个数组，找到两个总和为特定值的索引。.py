class Solution(object):

    def two_sum(self, nums, val):
        if nums is None or val is None:
            raise TypeError('nums or target cannot be None')
        if not nums:
            raise ValueError('nums cannot be empty')
        lenth = len(nums)
        res = []
        for i in range(lenth):
            temp = val - nums[i]
            for j in range(lenth):
                if nums[j] == temp:
                    res.append(i)
                    res.append(j)
                    return res
        return None
