class BSTNode:
    def __init__(self, val=None): # This initiates the class
        self.left = None #This is how we are going to keep track of the left node
        self.right = None # This is how we are going to keep track of the right node
        self.val = val #Val is the inputted value from the function call. We keep track
        #of that value by turning it into an object. 

    def insert(self, val):
        if not self.val: 
            self.val = val #This sets self.val to the current value
            return

        if self.val == val: #If the value is already in the tree, then we simply return
            return

        if val < self.val:
            if self.left: #If the current value is less than the inserted value, insert on the left
                self.left.insert(val)   #This inserts the value
                return
            self.left = BSTNode(val) #This adds the nessisary node to point to the new value. 
            return

        if self.right: # If the current value is more than the inserted value, we insert to the right
            self.right.insert(val) #This inserts the value
            return
        self.right = BSTNode(val) # This adds the nessisary node to the tree with the new value. 

    def get_min(self):
        current = self #This replaces self with current in the following code. 
        while current.left is not None: #We are going left to get the minimum because the smallest value is left
            current = current.left # This sets the new current to the next branch down the left side of the tree
        return current.val # Returns the bottom left value

    def get_max(self):
        current = self #This replaces self with current in the following code.
        while current.right is not None: # We are going right down the tree because the largest value is right. 
            current = current.right # This sets the new current to the next branch down the right side of the tree
        return current.val # Returns the bottom right value

    def delete(self, val):
        if self == None: # If there is nothing in the tree there is nothing to delete
            return self
        if val < self.val: # If the value you are lookning to delete is smaller you want to go down the tree left. 
            self.left = self.left.delete(val)
            return self #
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val: #This is the end of the code that has the postive output if the value is there. 
            return True

        if val < self.val: # If the value is less than the current value, then we need to go down left. 
            if self.left == None: # If we make it to the bottom of the tree, then we return false. 
                return False
            return self.left.exists(val) #This recursively calls the function again. 

        if self.right == None: # (This is assuming that the value is greater than the current value)
            # If we make it to the bottom of the tree going down to the right then the value is not there. 
            return False
        return self.right.exists(val) # This recursively calls the function again. 

    def inorder(self, vals): # This function is all about printing the values in the tree in numerical order. 
        if self.left is not None: #
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
        

def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
    bst = BSTNode()
    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")

    print("4 exists:")
    print(bst.exists(4))
    print("2 exists:")
    print(bst.exists(2))
    print("12 exists:")
    print(bst.exists(12))
    print("18 exists:")
    print(bst.exists(18))

main()