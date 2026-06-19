# 1732. Find the Highest Altitude


# Approach:
# Store the prefix sum for each elem
# return the max value for this array

# T.C = O(n)
# S.C = O(n)


class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        n = len(gain)
        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + gain[i]
        
        return max(prefix)
        
        