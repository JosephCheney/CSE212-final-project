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

Problem to solve

Finish this remove function

It is important to note that there is a variaty of cases that need to be taken into account
 * Empty tree, this would return false
 * Value you are looking to replace is in the root node
 * The Value is not in the tree, this would also return false
 * Value has only a left child
 * Value has a right child only
 * The value has both a left and right children

Parent.child 
