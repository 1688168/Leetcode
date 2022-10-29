class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1

####
# class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # to remove duplicate
        nums.sort()
        res=[]
        for ii, vv in enumerate(nums):
            if nums[ii] > 0: break # the array is sorted already, we cannot have sum of two bigger
                                   # number equal to a smaller postive number
            if ii==0 or vv != nums[ii-1]: # handle duplicate

                #two sum
                ll, rr = ii+1, len(nums)-1
                while ll < rr:
                    ttl=nums[ii]+nums[ll]+nums[rr]
                    if ttl == 0:
                        res.append((nums[ii], nums[ll], nums[rr]))
                        ll+=1
                        while ll < rr and nums[ll]==nums[ll-1]:
                            ll+=1
                    elif ttl > 0:
                        rr-=1
                    else:
                        ll+=1

        return res