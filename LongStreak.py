class Solution:
    def longestConsecutive(self,nums):
        # nums.sort()
        LongStreak = 0 
        numberSet = set(nums)
        for num in numberSet:
            if num - 1 not in numberSet:
                currentNum = num
                currentStreak = 1
                while currentNum + 1 in numberSet:
                    currentNum += 1
                    currentStreak += 1
                LongStreak = max(LongStreak,currentStreak)
        return LongStreak

if __name__ == '__main__':
    # begin
    nums = [100,4,200,1,3,2]
    s = Solution()
    print(s.longestConsecutive(nums))