class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def display(self):
        print("Stack: ", self.stack)
s = Stack()
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Size")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter item to push: ")
        s.push(item)
    elif choice == '2':
        s.pop()
    elif choice == '3':
        s.size()
    elif choice == '4':
        s.display()
    elif choice == '5':
        print("Exiting ..")
        break
    else:
        print("Invalid Choice")