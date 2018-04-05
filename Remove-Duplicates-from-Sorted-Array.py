# Remove Duplicates from Sorted Array

# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 
# Example:
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

######### Since we need to perform thos removal in-place, we can not use set or dictionaries for storing seen elements.
######### For this case to perform removal we will be using an index variable which will in turn be used to modify the input array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lstLength = len(nums)
        
        if lstLength == 0 or lstLength == 1:
            return lstLength
        
        uniqueIndex = 0
        
        for i in range(0,lstLength-1):
            
            if nums[i] != nums[i+1]:
                nums[uniqueIndex] = nums[i]
                uniqueIndex = uniqueIndex + 1
        
        nums[uniqueIndex] = nums[lstLength-1]
        uniqueIndex = uniqueIndex + 1
        
        return uniqueIndex
        