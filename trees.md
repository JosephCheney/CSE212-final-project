# Introduction

Trees are a structured form of linked list with nodes that point downward to left and right. They have nodes underneath them which links to the root (the top one) or parent if you are past the root. And those nodes are connected to more children. When there is no connecting node underneath the current node then it is called a Leaf. 
What we are looking at today is the most useful form of a tree which is a Binary Search Tree (BST). These trees have some very specific properties. 

*	The left subtree of a node contains only nodes with keys lesser than the node’s key (or parent).
*	The right subtree of a node contains only nodes with keys greater than the node’s key (or parent).
*	The left and right subtree each must also be a binary search tree. 
*	There must be no duplicate nodes.

The version of the tree structure that is the most efficient is the Balanced Binary search tree because of the depth of the tree is minimized by having each of the left and right nodes filled as the tree progresses down. This also makes it easy to find the height as it is the number of nodes between the bottom and the top of the tree with no more than a single layer difference of height along the whole bottom of the tree. There are certain algorithms that keep BSTs balanced and one of them is an AVL Tree that automatically senses when a tree has become unbalanced and shifts everything around. 

## Why use this data Structure

We use this data structure because it is a very efficient way to look up data from a large data set. The reason that it is more efficient is because of the time being cut in half to search for something. Self-balancing BSTs are also flexible, in the sense that it's easy to extend them to efficiently record additional information or perform new operations.



## Visualization

![My image file](/images/tree.png)


This is what it looks like to add a value to a BST. The value looks at the value its on and goes left if the value is less or goes right if the value is greater
![My image file](/images/tree_add.png)

## Photos of the structure and the insertion


## Example Operations
1.	Inserting into a BST
This is a recursive operation because you need to know which location of the BST to insert a value. So, to put that value in the correct location you need to go through from the head (or top) of the tree and compare the left and the right values. If the value is larger or smaller the recursion will step down in the according direction

2.	Traverse a BST (Forward)
The point of doing so is to display the data that the tree is holding. We need to first create a generator function. We need to use an __iter__ class to start this process. Then inside this class function we write a for loop like “for item in collection” as collection is the __iter__. This will give the next value in the BST. 
Then to get this to ‘print’ we need to use the keyword yield. But there is more, the yield command provides the next value to the earlier ‘for’ loop that we created. Yield also acts like a return function but it does not stop the continuation of the flow of the function. This is special so the function can keep going when the __iter__ is called again. “yield from” is also a keyword that allows you to tell another function to do the yielding. This is also useful if you need your __iter__ function to call another function. 

	
3.    Inorder (Left, Root, Right)

4.  Preorder (Root, Left, Right)

5.  Postorder (Left, Right, Root)

6. Remove 

    It is important to note that there is a variaty of cases that need to be taken into account
    * Empty tree, this would return false
    * Value you are looking to replace is in the root node
    * The Value is not in the tree, this would also return false
    * Value has only a left child
    * Value has a right child only
    * The value has both a left and right children



## Big O
Only log(n) if it is a balanced binary search tree. 

Space = O(n)

Access = O(log n)

Search = O(log n)

Insertion = O(log n)

Deletion = O(log n)

## Problem to solve
```python
class BSTNode:
    def __init__(self, val=None):# This initiates the class
        self.left = None #This is how we are going to keep track of the left node
        self.right = None # This is how we are going to keep track of the right node
        self.val = val #Val is the inputted value from the function call. We keep track
        #of that value by turning it into an object. 
```

```python
    def insert(self, val):
        if not self.val:
            self.val = val #This sets self.val to the current value
            return

        if self.val == val: #If the value is already in the tree, then we simply return
            return

        if val < self.val:
            if self.left:#If the current value is less than the inserted value, insert on the left
                self.left.insert(val)  #This inserts the value
                return
            self.left = BSTNode(val) #This adds the nessisary node to point to the new value.
            return

        if self.right: # If the current value is more than the inserted value, we insert to the right
            self.right.insert(val) #This inserts the value
            return
        self.right = BSTNode(val) # This adds the nessisary node to the tree with the new value. 
```
```python
    def get_min(self):
        current = self
        while current.left is not None: #We are going left to get the minimum because the smallest value is left
            current = current.left # This sets the new current to the next branch down the left side of the tree
        return current.val # Returns the bottom left value

    def get_max(self):
        current = self
        while current.right is not None: # We are going right down the tree because the largest value is right.
            current = current.right # This sets the new current to the next branch down the right side of the tree
        return current.val # Returns the bottom right value
```

```python
    def delete(self, val):
        if self == None: # If there is nothing in the tree there is nothing to delete also checks if self is not deleted yet
            return self
        if val < self.val: # If the value you are lookning to delete is smaller you want to go down the tree left.
            if self.left:
                self.left = self.left.delete(val) # This recursively calls the function one step down the tree one left
            return self # If the function gets there then the value to delet is not in the tree. 
        if val > self.val: # If the value you are looking to delete is larger, you want to go down the tree to the right. 
            if self.right:
                self.right = self.right.delete(val) # This recursively calls the function one step down the tree to the right
            return self # If the function gets here then the value to delete is not in the tree
        if self.right == None: # This is checking to see if there is more tree further down to the right.
            return self.left
        if self.left == None: # This is checking to see if there is more tree further down to the left. 
            return self.right
        min_larger_node = self.right #This sets the node to the right as the larger node
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        
        return self

  ``` 
     
  ```python
  
    def exists(self, val):
        if val == self.val:#This is the end of the code that has the postive output if the value is there.
            return True

        if val < self.val: # If the value is less than the current value, then we need to go down left.
            if self.left == None: # If we make it to the bottom of the tree, then we return false.
                return False
            return self.left.exists(val) #This recursively calls the function again. 

        if self.right == None:# (This is assuming that the value is greater than the current value)
            # If we make it to the bottom of the tree going down to the right then the value is not there.
            return False
        return self.right.exists(val) # This recursively calls the function again.
```

```python
    def preorder(self, vals): # Preorder = (Root, Left, Right)
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals): #Inorder = (Left, Root, Right)
        #Write the code that will put the values in order and return them

    def postorder(self, vals): #Postorder = (Left, Right, Root)
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals
```
```python
def main():
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18, 2]
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
    print(bst.inorder([]))
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
```
Finish this remove function

It is important to note that there is a variaty of cases that need to be taken into account
 * Empty tree, this would return false
 * Value you are looking to replace is in the root node
 * The Value is not in the tree, this would also return false
 * Value has only a left child
 * Value has a right child only
 * The value has both a left and right children

Parent.child 
