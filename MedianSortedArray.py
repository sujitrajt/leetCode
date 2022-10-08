class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        ptr1 = 0 
        ptr2 = 0 
        combinedList = []
        while ptr1 < len(nums1) and ptr2 < len(nums2) : 
            if nums1[ptr1] < nums2[ptr2]:
                combinedList.append(nums1[ptr1])
                ptr1 += 1 
            else: 
                combinedList.append(nums2[ptr2])
                ptr2 += 1 
        if ptr1 == len(nums1) :
            combinedList += nums2[ptr2:]
        elif ptr2 == len(nums2):
            combinedList += nums1[ptr1:]
        lengthOfList = len(combinedList)
        print(lengthOfList)
        print(combinedList)
        if lengthOfList % 2 == 0 : 
            middle = lengthOfList // 2 
            # print(middle)
            median = (combinedList[middle] + combinedList[middle - 1 ]) / 2
            print(combinedList[middle])
            print(combinedList[middle - 1])
            print(median)
        else : 
            middle = lengthOfList // 2 
            median = combinedList[middle]
        return median

