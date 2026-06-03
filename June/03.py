# Earliest Finish Time for Land and Water Rides II

# Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
# Output: 9


# This problem is same as yesterday's problem the only change is no of constraints is very large in it so the previous solution gives TLE. So we have to optimize that solution.


# Approach:

# In this approach we are fixing one ride and then getting the min possible time for second time. 
# so for first ride finish time F, seond ride total time will be :  
# = max(F, start time of 2nd ride) + dur of 2nd ride. 

# Now here the start time of 2nd ride can be either <= F or > F.

# If start2nd ≤ F:  total = F + dur2nd (means we can immediately start 2nd ride)

# If start2nd > F:   total = start2nd + dur2nd (we have to start from 2nd ride start time)


# ✨Key insight: For a fixed F, we don't need to check every j. We just need:

# 1. Minimum duration among rides with start ≤ F
# 2. Minimum (start + duration) among rides with start > F


# The Precomputation Idea 
# If we sort the second rides by start time, we can precompute:


# prefix_min_duration[k] = min duration among first k rides
# suffix_min_sum[k] = min (start+duration) among rides from k to end

# Now for any F:
# Binary search to find split point k (first ride with start > F)
# Best = min(F + prefix_min_duration[k-1], suffix_min_sum[k])


# Complete Flow: --------------------------------------------------

# Problem: Pick two rides (order matters) to minimize finish time
#     ↓
# Observation: For fixed first ride, second ride's contribution has two cases
#     ↓
# Insight: Split into "early" (start ≤ F) and "late" (start > F) rides
#     ↓
# Key: For early rides, only duration matters; for late, only sum matters
#     ↓
# Solution: Sort second rides, precompute prefix min duration & suffix min sum
#     ↓
# For each first ride: binary search split point, O(log m) per query
#     ↓

# Time complexity: O((n+m) log m)




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

        # Create and sort rides
        land_rides = []
        for i in range(n):
            land_rides.append([startl[i], durl[i]])

        water_rides = []
        for i in range(m):
            water_rides.append([startw[i], durw[i]])
        
        land_rides.sort()
        water_rides.sort()
        
        def min_finish_time(first_rides, second_rides):
            # Precompute for second_rides:
            # 1. Prefix min duration
            # 2. Suffix min of (start + duration)

            m = len(second_rides)
            prefix_min_dur = [float('inf')] * m
            suffix_min_sum = [float('inf')] * (m + 1)
            
            for i in range(m):
                if i == 0:
                    prefix_min_dur[i] = second_rides[i][1]
                else:
                    prefix_min_dur[i] = min(prefix_min_dur[i-1], second_rides[i][1])
            
            for i in range(m-1, -1, -1):
                suffix_min_sum[i] = min(suffix_min_sum[i+1], second_rides[i][0] + second_rides[i][1])
            
            # Process each first ride using binary search
            min_time = float('inf')
            
            for start, dur in first_rides:
                F = start + dur
                
                # Binary search to find first index with start > F
                left, right = 0, m
                while left < right:
                    mid = (left + right) // 2
                    if second_rides[mid][0] <= F:
                        left = mid + 1
                    else:
                        right = mid
                
                ptr = left  # first index with start > F
                
                # Rides with start <= F (indices 0 to ptr-1)
                if ptr > 0:
                    min_time = min(min_time, F + prefix_min_dur[ptr-1])
                
                # Rides with start > F (indices ptr to m-1)
                if ptr < m:
                    min_time = min(min_time, suffix_min_sum[ptr])
            
            return min_time
        
        # Try both orders
        ans = min(min_finish_time(land_rides, water_rides),
                  min_finish_time(water_rides, land_rides))
        
        return ans
    


if __name__ == "__main__":
    sol = Solution()

    lst = [2,8]
    ld = [4,1]
    wst = [6]
    wd = [3]
    print(sol.earliestFinishTime(lst,ld,wst,wd))

