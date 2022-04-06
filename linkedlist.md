# Introduction

This data structure is very unique in the sense that it has a node with a value and a pointer towards the next node and so on until the end of the data. And doubly linked lists have pointers towards the node before (or previous)

## Why use this data Structure

This data structure is not the most memory efficient but is the most useful when you need to delete the first value in the 'list' or when you need to add something to the first value of the list of values.  



## Visualization

![My image file](/images/DLL1.png)



## Example Operations

1. insert_head

    This adds a value to the first item in the linked list. What it needs to do is to add a pointer to the first item currently in the list that points back to the new value and add a ponter to the new value that ponts to the old head.

2. insert_tail

    This adds a value to the end of the linked list. What it needs to do is to add a pointer to the tail of the list that points to the new value we are adding and add a pointer from the new tail to the old tail. 
3. insert (value)

    This adda a value anywhere on the doubly linked list. What you need to do is figure out where you are going to insert the value (typically numerical oreder) and then you need to replace the pointers of the values on both sides so they pont to the new value you are inserting. 
4. remove head

    This function takes the head pointers and removes them and takes the pointer from the second value to the first and removes it. This effectively takes off the head at the neck.  We don't need to worry about deleting the value at the head because python will delete it automatically at clean up. 
5. remove_tail

    This function removes the last value in the linked list. This is done by removing the ponters that point to and from the tail of the list. And the tail gets deleted by the python clean up. 
6. remove(value)

    This function removes a value from the list. First you need to traverse the list and find the node with the value. Then to get rid of that value simply change all of the pointers to bypass the value you are deleting and point to the node before and after. 
7. size()

    This function returns the size of the list. It does this by using the size function on where the linked list is stored. 
8. empty()

    This function returns true if the list is empty. Really this does a simple logic check for if empty return true. 
## Big O
insert_head(value) =	O(1) 

insert_tail(value) =	O(1) 

insert(i, value) = O(n) 

remove_head()  = O(1)

remove_tail(index) = O(1)

remove(i) = O(n)

size() = O(1)

empty() = 	O(1) 


## Problem to solve



```python



```

[Here is a link to the code](stack.py)


[Trees](trees.md)

[Linked Lists](list.md)