#Binary_Search_tree
class Node:
    def __init__(self,item=None,left=None,right=None):
       self.item=item
       self.left=left
       self.right=right
class BST:
    def __init__(self):
         self.root=None
    def insert(self,):
        self.root=self.r_insert(self.root,data)           
    def r_insert(self,root,data):
        if root is None:
            return Node(data)
        elif data<root.item:
            root.left=self.r_insert(root.left,data)
        elif data>=root.item:
            root.right=self.r_insert(root.right,data)
        return root        
    def search(self,data):
        return self,r_search(self.root,data)
    def r_search(self,root,data):
        if root is None or root.item==data:
            return root
        elif data<root.item:
            return self.r_search(root.left,data)
        else:
            return self.r_search(root.right,data)    
    def inorder(self):
        result=[]            
        self.r_inorder(self.root,result)
        return result
    def r_inorder(self,root,result):
        if root :
            self.r_inorder(root.left,result)
            result.append(root.item)
            self.r_inorder(root.right,result)
            
    def pre_order(self):
        result=[]            
        self.r_pre_order(self.root,result)
        return result
    def r_pre_order(self,root,result):
        if root :
            result.append(root.item)
            self.r_pre_order(root.left,result)
            self.r_pre_order(root.right,result)
            
    def post_order(self):
        result=[]            
        self.r_post_order(self.root,result)
        return result
    def r_post_order(self,root,result):
        if root :
            result.append(root.item)
            self.r_post_order(root.left,result)
            self.r_post_order(root.right,result)
            
            