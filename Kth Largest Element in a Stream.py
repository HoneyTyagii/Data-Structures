# 703. Kth Largest Element in a Stream

# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

# Example 1:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
 

# Constraints:

# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you search for the kth element.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
    
# 2 approach

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums[:k]
        self.k = k
        heapify(self.nums)
        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                heappushpop(self.nums, nums[i])
        
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif val > self.nums[0]:
            heapreplace(self.nums, val)
        
        return self.nums[0]