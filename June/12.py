# 3559. Number of Ways to Assign Edge Weights II


# This problem is extended version of yesterdays problem.
# So here for each query we need to get edge_cnt and then find total odd ways: 2^(ed-1)

# Now here the constraints are very large.
# So we need efficient way to count edge b/n both nodes in each query.


# Count edges b/n 2 nodes:
# I already have solved this problem. 
# The formula i was using : dist[u]+dist[v]-2*dist[lca]

# LCA  - Lowest common ancestor

# So here write a dfs and inside it use dist, parent arry.
# dist will be helpful and parent will helpful for lca and also will work like visited arry.


# Although this solution is correct but it gives TLE 🥲.
# So todays pod point is missed. 


class Solution(object):
    def assignEdgeWeights(self, edges, queries):

        MOD = 1000000007

        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parents = [0] * (n + 1)
        depth = [0] * (n + 1)

        def dfs(node, parent, level):
            parents[node] = parent
            depth[node] = level

            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node, level + 1)

        dfs(1, 0, 0)

        def lca(u, v):

            while depth[u] > depth[v]:
                u = parents[u]

            while depth[v] > depth[u]:
                v = parents[v]

            while u != v:
                u = parents[u]
                v = parents[v]

            return u

        ans = []

        for u, v in queries:

            ancestor = lca(u, v)

            edge_count = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            if edge_count == 0:
                ans.append(0)
            else:
                ans.append(
                    pow(2, edge_count - 1, MOD)
                )

        return ans


