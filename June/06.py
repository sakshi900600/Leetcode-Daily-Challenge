# Left and Right Sum Differences


# Approach:
# Just calculated the left sum and right sum for all elem and stored resutlts into 2 lists.
# took a final ans list and stored the abs diff of left and right sum.

# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        left_sum = [0]*n
        right_sum = [0]*n

        for i in range(1,n):
            left_sum[i] = left_sum[i-1] + nums[i-1]
        
        for i in range(n-2,-1,-1):
            right_sum[i] = right_sum[i+1] + nums[i+1]
        

        ans = [0]*n
        for i in range(n):
            ans[i] = abs(left_sum[i] - right_sum[i])
        

        print(left_sum, right_sum)
        return ans
        


        