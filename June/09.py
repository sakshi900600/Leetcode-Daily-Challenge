# 3689. Maximum Total Subarray Value I

# Here we have to get k subarr and calculate a val = max-min of that subarr.
# get the total as the sum of all val. we can take any subarr any no of times
# and return max total value possible

# Input: nums = [4,2,5,1], k = 3
# Output: 12

# Explanation:
# One optimal approach is:

# Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
# Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
# Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.
# Adding these gives 4 + 4 + 4 = 12.



# Approach
# max values we can get when we take the whole arr's max,min.
# so i first calculated val as the diff of max, min of whole arr
# added it k times into total
# return total values


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        val = max(nums) - min(nums)
        total = 0

        for i in range(k):
            total += val
        
        return total
        