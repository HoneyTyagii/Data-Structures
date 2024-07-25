# 912. Sort an Array

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right) 

    def merge(self, left, right):
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged

    def sortArray(self, nums):
        return self.merge_sort(nums)
    
# 2 Approach
    
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(low, mid, high):
            res = [0] * (high - low + 1)
            i = low
            j = mid + 1
            k = 0
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    res[k] = nums[i]
                    i += 1
                    k += 1
                else:
                    res[k] = nums[j]
                    j += 1
                    k += 1
            while i <= mid:
                res[k] = nums[i]
                i += 1
                k += 1
            while j <= high:
                res[k] = nums[j]
                j += 1
                k += 1
            for x in range(len(res)):
                nums[low + x] = res[x]
        def mergeSort(low, high):
            if low < high:
                mid = low + (high - low) // 2
                mergeSort(low, mid)
                mergeSort(mid + 1, high)
                merge(low, mid, high)
        mergeSort(0, len(nums) - 1)
        return nums