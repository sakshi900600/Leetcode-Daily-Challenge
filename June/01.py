# 2144. Minimum Cost of Buying Candies With Discount
# Input: cost = [6,5,7,9,2,2]
# Output: 23


# Logic:
# Through example observed that if we sort cost in descending order and then everytime take 2 candy and 1 candy for free and repeat then our job will be done. 


# So, added all cost in max-heap
# till mh size >=2 pop 2 candy and add its cost in a mincost var and pop another free candy. 
# at the end checked if any candy left, then add its cost in mincost var.
# if only 1 elem in array then that will be the mincost. 


# tc = O(nlogn), coz 1 heap operation takes logn and here we have total n elem. 
# sc = O(n), coz storing all elem in heap.


import heapq
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        if len(cost)==1:
            return cost[0]

        max_heap = []

        for c in cost:
            heapq.heappush(max_heap, -c)
        
        mincost = 0
        while len(max_heap) >= 2:
            c1 = heapq.heappop(max_heap)
            c2 = heapq.heappop(max_heap)
            val = -c1-c2
            mincost += val

            if len(max_heap) >= 1:
                heapq.heappop(max_heap)
        
        if len(max_heap) > 0:
            c = heapq.heappop(max_heap)
            mincost += -c
            
        return mincost
        
        