



# Brute force soln:

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        max_heap = []
        n = len(nums)

        for i in range(n):
            for j in range(i,n):
                subarr = nums[i:j+1]
                val = max(subarr)-min(subarr)
                heapq.heappush(max_heap, -val)
        
        cnt = 0
        total = 0
        while max_heap:
            val = heapq.heappop(max_heap)
            val = -val
            total += val
            cnt += 1
            if cnt == k:
                break
        
        return total


        
# Using Segment Tree:
class Solution2(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)
        if n == 1:
            return 0
        
        minSt = SegmentTree(nums, True) # True for min segment tree
        maxSt = SegmentTree(nums, False) # False for max segment tree

        # get value(max-min) for range (l..r)
        def getValue(l,r):
            minv = minSt.query(l,r)
            maxv = maxSt.query(l,r)
            return maxv-minv
        
        max_heap = []
        # put all the best values i.e from (l..n-1) into heap
        for l in range(n):
            val = getValue(l,n-1)
            heapq.heappush(max_heap, (-val, l, n-1))
        

        # get best k values
        total = 0
        for _ in range(k):
            val,l,r = heapq.heappop(max_heap)
            total -= val

            # put the next best value
            if l < r:
                nextVal = getValue(l,r-1)
                heapq.heappush(max_heap, (-nextVal, l, r-1))
        
        return total



class SegmentTree:
    def __init__(self, arr, is_min):
        self.n = len(arr)
        self.is_min = is_min

        self.tree = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1, arr)

    def build(self, node, start, end, arr):

        if start == end:
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2

        self.build(2 * node, start, mid, arr)
        self.build(2 * node + 1, mid + 1, end, arr)

        if self.is_min:
            self.tree[node] = min(
                self.tree[2 * node],
                self.tree[2 * node + 1]
            )
        else:
            self.tree[node] = max(
                self.tree[2 * node],
                self.tree[2 * node + 1]
            )

    def query(self, left, right):
        return self._query(
            1,
            0,
            self.n - 1,
            left,
            right
        )

    def _query(self, node, start, end, left, right):

        # no overlap
        if end < left or start > right:
            if self.is_min:
                return float('inf')
            return float('-inf')

        # complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # partial overlap
        mid = (start + end) // 2

        left_ans = self._query(
            2 * node,
            start,
            mid,
            left,
            right
        )

        right_ans = self._query(
            2 * node + 1,
            mid + 1,
            end,
            left,
            right
        )

        if self.is_min:
            return min(left_ans, right_ans)

        return max(left_ans, right_ans)

        