# 2161. Partition Array According to Given Pivot


# Input: nums = [9,12,5,10,14,3,10], pivot = 10
# Output: [9,5,3,10,10,12,14]


# Approach:
# Created 3 list: left for smaller , right for larger and equal for same elem as pivot.
# created an ans list and extended all three list in smaller,equal,larger order.
# returned the list

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        n = len(nums)
        left = []
        right = []
        equal = []

        for i in range(n):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
            else:
                equal.append(nums[i])
        
        ans = []
        ans.extend(left)
        ans.extend(equal)
        ans.extend(right)

        return ans


        