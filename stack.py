# This class represents a stack (LIFO)
class Stack(object):
    # Constructor function to create an empty stack
    def __init__(self):
        self.items = [] # The stack is represented as a list of items

    # This function checks if the stack is empty
    def isEmpty(self):
        if len(self.items) > 0: # If there are items in the list, the stack is not empty
            return False
        return True # If there are no items, te stack is empty

    # This function clears all the items from the stack
    def clear(self):
        self.items = [] # Reset the list to an empty state

    # This function adds a new item to the top of the stack
    def push(self, item):
        self.items.append(item) # Add the new item to the end of the list (top of the stack)

    # This function removes the item from the top of the stack
    def pop(self):
        if not self.isEmpty(): # Check if the stack is not empty
            removedItem = self.items.pop(len(self.items) - 1) # Remove and return the last item in the list
            return removedItem
        return None # If the stack is empty, return None

    # This function looks at the item at the top of the stack without removing it
    def peek(self):
        if not self.isEmpty(): # Check if the stack is not empty
            return self.items[len(self.items) - 1] # Return the last item in the list
        return None # If the stack is empty, return None