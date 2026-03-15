# 1622. Fancy Sequence

# Hard

# Write an API that generates fancy sequences using the append, addAll, and multAll operations.

# Implement the Fancy class:

# Fancy() Initializes the object with an empty sequence.
# void append(val) Appends an integer val to the end of the sequence.
# void addAll(inc) Increments all existing values in the sequence by an integer inc.
# void multAll(m) Multiplies all existing values in the sequence by an integer m.
# int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
 

# Example 1:

# Input
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# Output
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]

# Explanation
# Fancy fancy = new Fancy();
# fancy.append(2);   // fancy sequence: [2]
# fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
# fancy.append(7);   // fancy sequence: [5, 7]
# fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // return 10
# fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
# fancy.append(10);  // fancy sequence: [13, 17, 10]
# fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // return 26
# fancy.getIndex(1); // return 34
# fancy.getIndex(2); // return 20
 

# Constraints:

# 1 <= val, inc, m <= 100
# 0 <= idx <= 105
# At most 105 calls total will be made to append, addAll, multAll, and getIndex.

class Fancy:
    MOD = 1000000007

    def __init__(self):
        self.global_mul = 1
        self.global_mul_inv = 1
        self.global_add = 0
        self.base_values = []

    def append(self, val: int) -> None:
        new_val = (val - self.global_add) * self.global_mul_inv % self.MOD
        self.base_values.append(new_val)

    def addAll(self, inc: int) -> None:
        self.global_add = (self.global_add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.global_mul = self.global_mul * m % self.MOD
        self.global_add = self.global_add * m % self.MOD

        inv_m = pow(m, self.MOD - 2, self.MOD)
        self.global_mul_inv = self.global_mul_inv * inv_m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.base_values):
            return -1
        return (self.base_values[idx] * self.global_mul + self.global_add) % self.MOD