from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        """Pushes an element onto the stack."""
        self.q.append(x)
    
    def pop(self):
        """Removes and returns the top element of the stack."""
        if self.empty():
            return None  # Return None if stack is empty

        # Move all elements except the last one to the back of the queue
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        return self.q.popleft()  # Remove and return the last element (top of stack)

    def top(self):
        """Returns the top element of the stack without removing it."""
        if self.empty():
            return None  # Return None if stack is empty
        return self.q[-1]  # Last inserted element is at the end of the queue

    def empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return len(self.q) == 0

# Example Usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())   # Output: 3 (top element)
print(stack.pop())   # Output: 3 (removes top element)
print(stack.top())   # Output: 2 (new top element)
print(stack.pop())   # Output: 2
print(stack.pop())   # Output: 1
print(stack.empty()) # Output: True (stack is now empty)
