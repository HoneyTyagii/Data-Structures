# 4. Median of Two Sorted Arrays

# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2, nums1 # nums1 is smaller
        
        m,n = len(nums1), len(nums2)
        imin, imax , half_len = 0,m , (m + n + 1) //2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i < m and nums2[j - 1] > nums1[i]: # i is too small , increase it to 
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i==0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1],nums2[j-1])

                if(m+n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j ==n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i],nums2[j])

                return(max_left + min_right) / 2    


# time complexity: O(log(min(m,n)))
# space complexity: O(1)
