# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        #init an array to store values that will eventually
        #be joined as a string -- easy to append
        ans = []

        #depth first search, accepting the current node the 
        #program is on
        def dfs(node):
            #if there is no node (i.e., the node is NULL),
            #append key word N: N is NaN so will be like a 
            #key word
            if not node:
                ans.append("N")
                #return to end func
                return

            #append the val from the node to the array
            #notice we're following a depth first search 
            #approach. So, we must unpack in the same way later
            ans.append(str(node.val))

            #call dfs on left node, then right
            #completely explore left side, then ram stack goes
            #all the way back up to the right
            dfs(node.left)
            dfs(node.right)
        
        #call our dfs function, starting at the root
        dfs(root)

        #join the array to a string '#' as our keyword
        return "#".join(ans)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #start by init an arr, splitting the data by our
        #keyword '#'
        arr = data.split("#")

        #use self.i rather than i so that we dont remake
        #a local variable whenever we iterate

        #i will serve as our index, and be altered as a 
        # side effect
        self.i = 0

        #make a new dfs function to unpack
        def dfs():
            #if the val is "N" that means the node is null
            #so, simply increase the index and return none
            if arr[self.i] == "N":
                self.i += 1
                return None

            #create new node with appropraite value in the arr
            node = TreeNode(arr[self.i])
            #increase index
            self.i += 1
            #call dfs on left and then right, as we used dfs
            #in serialization too
            node.left = dfs()
            node.right = dfs()
            #after stack is complete, return the node
            return node

        return dfs()
