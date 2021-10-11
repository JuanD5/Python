#%%
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
root = [1,'null',2,3]
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else [] # left, root, right 

    def preorder(root):
        return [root.val] + preorder(root.left) + preorder(root.right) if root else []   # root , left , right 

    def postorder(root):
        return  postorder(root.left) + postorder(root.right) + [root.val] if root else []    
        

#%%
# binary tree max sumpath 

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf") # placeholder to be updated
        def get_max_gain(node):
            nonlocal max_path # This tells that max_path is not a local variable
            if node is None:
                return 0    
            gain_on_left = max(get_max_gain(node.left), 0) # le preguntamos a ese nodo si su valor izquierdo es mayor a 0 
            gain_on_right = max(get_max_gain(node.right), 0)  # le preguntamos a ese nodo si su valor derecho es mayor a 0 
                
            current_max_path = node.val + gain_on_left + gain_on_right # el valor máximo es el valor de ese nodo mas la ganancia máxima de la izquierda y la de la derecha 
            max_path = max(max_path, current_max_path) # se actualiza el valor del maxpath 
                
            return node.val + max(gain_on_left, gain_on_right) # al final el path será el valor de ese nodo + el valor máximo entre la ganancia de la izquierda y la derecha , solo hay un path 

        get_max_gain(root) # Starts the recursion chain
        return max_path	        