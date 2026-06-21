# 1833. Maximum Ice Cream Bars


class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """

        costs.sort()
        cnt = 0

        for i in range(len(costs)):
            if coins >= costs[i]:
                cnt += 1
                coins -= costs[i]
        
        return cnt
        