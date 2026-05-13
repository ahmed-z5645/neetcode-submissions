# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # init ans array
        res = []


        #depth first search, recursive helper function
        # as the program traverses the tree, it keeps count of depth,
        # and then appends to the appropriate sub array in 2d array
        def dfs(node, depth):
            # if no node, return none
            if not node: return None

            #if the len of current depth, append an empty list
            #remeber that len gives index + 1
            if len(res) == depth:
                res.append([])

            # append the value at the correct depth
            res[depth].append(node.val)

            # call dfs again on the left and right node,
            # adding + 1 to the depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        # call dfs at root, with depth of 0 (index 0)
        dfs(root, 0)

        #after recursive stack is finished, return answer
        return res