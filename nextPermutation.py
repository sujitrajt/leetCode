class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lengthOfList = len(nums) 
        pivot = 0 
        swap = lengthOfList - 1 
        #Iterating from Back and finding the peak element and setting it as pivot 
        for i in range(lengthOfList - 1, 0 , -1):
            if nums[i-1] < nums[i]:
                pivot = i 
                break 
        if pivot == 0 : 
            return nums.sort()
        # finding the greater element of pivot - 1 
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1 
        # swap it 
        nums[swap],nums[pivot-1] = nums[pivot-1], nums[swap]
        nums[pivot:] = sorted(nums[pivot:])
            