import copy

class Stack:
    def __init__(self):
        self.stack = []

    def add_value(self, value):
        self.stack.append(value)
    
    def remove_last_value(self):
        return self.stack.pop()
    
    def print_stack(self):
        stack_copy = copy.copy(self.stack)
        while len(stack_copy) > 0:
            last_value = stack_copy.pop()
            print (last_value)
        
    def count_days(self):
        '''Counts the number of days it will take to wear all of the shirts'''
        
        count = len(self.stack)
        print (count)




#This is the Test       
stack = Stack()
stack.add_value("red")
stack.add_value("Dorito")
stack.add_value("Plad")
stack.add_value("Superman")
stack.add_value("red")
stack.add_value("green")
stack.add_value("BYUI")
stack.count_days() #This should return the length of the stack. 
#This prints the stack in A LIFO order
stack.print_stack()
#expected value == (BYUI, green, red, Superman, Plad, Dorito, Red)
print()
print()
stack.remove_last_value()
stack.print_stack()
# Expect to have taken off and worn the BYUI shirt