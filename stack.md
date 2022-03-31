# Introduction

The data structure of a stack is exactly what it sounds like. In essense you are looking at the data as if it were a stack of paper on a desk. You put a piece of paper on that desk and if you place another, you would need to remove the top one in order to get to the bottom sheet. Our computers do this naturally if you think of a back arrow on a browser, the data in the browser is stored in order in a stack. When you are writing a paper or code and you do control Z to undo, the computer knows what to undo because it is keeping a stack of memory of your previous actions. 

## Why use this data Structure

This data structure is very useful when you need to keep track of the order of the actions/ data. It is also very easy to reverse data if you think about it. The first in a stack has to be the last one out. If you input a word in a stack then print that same word from the stack, the result would be a backwards version.  



## Visualization

![My image file](/images/stack.webp)



## Example Operations

1. Push - This adds a value to the end of the stack 
2. Pop - This deletes the last item in the stack (or top of the stack)
3. Print Stack - This prints the stack as Last In First Out (Reverse order)

## Big O
Push = O(1)

Pop = O(1)

Print  = O(n)

## Problem to solve

You have a stack of Shirts in your drarw and you want to wear them in order of the top of the stack to the bottom before you do laundry, impliment some code that will output the correct wear order of the shirts. 

```python

import copy

class Stack:
    def __init__(self):
        self.stack = []

    def add_value(self, value):
        self.stack.append(value)
    
    def remove_last_value(self):
        return self.stack.pop()
    
    def print_stack(self):
        ''' Add the code that will print the stack in the LIFO order. Hint: make a copy of the stack
        pass 
        


#This is the Test       
stack = Stack()
stack.add_value("red")
stack.add_value("Dorito")
stack.add_value("Plad")
stack.add_value("Superman")
stack.add_value("red")
stack.add_value("green")
stack.add_value("BYUI")

#This prints the stack in A LIFO order
stack.print_stack()
#expected value == (BYUI, green, red, Superman, Plad, Dorito, Red)
print()
print()


stack.remove_last_value()
stack.print_stack()

```

[Here is a link to a solution](stack.py)
