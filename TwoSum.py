class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hashMap : 
                hashMap[nums[i]] = i
            else : 
                return [i, hashMap[complement]]
if __name__ == '__main__':
    nums = [2,7,11,15], 
    target = 9
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))