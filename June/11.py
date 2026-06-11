# 3558. Number of Ways to Assign Edge Weights I


# We are given 1 to n nodes of tree and edges. You have to assign either 0 or 1 weight to edges

# The cost of a path between any two nodes u and v is the total weight of all edges in the path connecting them.

# select any node at maximum depth. 
# Return the number of ways to assign edge weights in the path from node 1 to x such that its total cost is odd. 



# Approach:
# Here the given tree is not binary tree. But we will use the similar approach to get depth as in tree.
# In tree we were getting the lh,rh and doing 1 + max(lh,rh)

# Coz here the tree is not binary so we will first build adj list.
# then for each neigh in adj[node]:
# we will do recursive call for the neigh nodes and add 1.
# store maxdepth into a var
# return maxdepth from the function.


# on any maxdepth total possible ways to assing weight is 2^d coz we have 2 options either 1 or 2.
# from all those options

# Ex - d=2
# 11 = 1+1 = 2
# 12 = 1+2 = 3
# 21 = 2+1 = 3
# 22 = 2+2 = 4

# odd posibility == even possibility
# odd + even = total = 2^d
# 2.odd = 2^d
# odd = 2^(d-1)




class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        mod = 1000000007

        n = len(edges)+1 # no of nodes

        adj = [[] for _ in range(n+1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        d = self.getMaxDepth(adj, 1, -1)

        return pow(2, d-1) % mod

    
    def getMaxDepth(self, adj, node, parent):
        depth = 0
        for neigh in adj[node]:
            if neigh == parent:
                continue
            
            depth = max(depth, 1 + self.getMaxDepth(adj,neigh,node))
        
        return depth
    



        