# 2196. Create Binary Tree From Descriptions

# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]

#           50
#         /    \
#       20      80
#      /  \     /
#   15     17  19


# Approach:



# Time Complexity: O(n)
# Space Complexity: O(n)






# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        # dict: node_val -> [children_list, parent_list]
        # children_list contains tuples (child_val, isLeft)
        node_info = {}

        for parent, child, isLeft in descriptions:

            if parent not in node_info:
                node_info[parent] = [[], []]  
            
            if child not in node_info:
                node_info[child] = [[], []]

            node_info[parent][0].append((child, isLeft))

            node_info[child][1].append(parent)
        

        root_val = None
        for node_val, info in node_info.items():
            if len(info[1]) == 0: 
                root_val = node_val
                break
        

        root = TreeNode(root_val)
        

        def buildTree(node):
            if not node:
                return None
            
            node_val = node.val
            if node_val in node_info:
                children = node_info[node_val][0]
                
                for child_val, isLeft in children:
                    child_node = TreeNode(child_val)
                    
                    if isLeft == 1:
                        node.left = child_node
                    else:
                        node.right = child_node
                    
                    # Recursively build the child's subtree
                    buildTree(child_node)
            
            return node

        return buildTree(root)
        