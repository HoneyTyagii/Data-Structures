class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                counter += 1
        return counter

#itertive solution

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(column) != sorted(column) for column in zip(*strs))