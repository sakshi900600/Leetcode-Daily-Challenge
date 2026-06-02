def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
    n, m = len(landStartTime), len(waterStartTime)
    min_time = float('inf')
    
    # Case 1: Land first, then water
    for i in range(n):
        land_finish = landStartTime[i] + landDuration[i]
        for j in range(m):
            water_start = max(land_finish, waterStartTime[j])
            total_time = water_start + waterDuration[j]
            min_time = min(min_time, total_time)
    
    # Case 2: Water first, then land
    for j in range(m):
        water_finish = waterStartTime[j] + waterDuration[j]
        for i in range(n):
            land_start = max(water_finish, landStartTime[i])
            total_time = land_start + landDuration[i]
            min_time = min(min_time, total_time)
    
    return min_time




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
    
    