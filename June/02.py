# Earliest Finish Time for Land and Water Rides I
# Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
# Output: 9


# Approach:
# Here we have to find out min time to finish 2 rides. 
# Now we have 2 possibilities
# 1. Either first start land ride then water or
# 2. frist start water ride then land.

# In both ways we will find out min time and 
# at the end return the smallest value from both ways.


# for either ways: 1st finish time will be equal to start+dur time of it.
# then for next ride, their start will be max(last ride finish, start time of curr ride) and total as whatever start val we get + dur
# store min of it.
# return smallest of both min .


# Time Complexity: O(n*m) or O(n^2) if n and m are of same size.
# Space Complexity: O(1)



class Solution(object):

    def earliestFinishTime(self, startl, durl, startw, durw):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        
        n = len(startl)
        m = len(startw)
        
        landmin = float("inf")
        watermin = float("inf")

        # all combo for land -> water
        for i in range(n):
            lf = startl[i] + durl[i]
            for j in range(m):
                ws = max(lf,startw[j])
                total = ws + durw[j]
                landmin = min(landmin, total)

        
        # all combo for water -> land
        for j in range(m):
            wf = startw[j] + durw[j]
            for i in range(n):
                ls = max(wf, startl[i])
                total = ls + durl[i]
                watermin = min(watermin, total)
        
        return min(landmin, watermin)



    # combined 2 loops into 1.
    def earliestFinishTime2(self, startl, durl, startw, durw):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        
        n = len(startl)
        m = len(startw)
        
        ans = float('inf')
        
        # Try every land-water ride pair
        for i in range(n):
            for j in range(m):
                # Case 1: Land -> Water
                land_finish = startl[i] + durl[i]
                finish1 = max(land_finish, startw[j]) + durw[j]
                
                # Case 2: Water -> Land
                water_finish = startw[j] + durw[j]
                finish2 = max(water_finish, startl[i]) + durl[i]
                
                # Update answer with both possibilities
                ans = min(ans, finish1, finish2)
        
        return ans
    
    