# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,item):
#         self.stack.append(item)
#     def pop(self):
#         if len(self.stack) < 1:
#             return None
#         return self.stack.pop()
#     def size(self):
#         return len(self.stack)
    
# s = Stack()
# while True:
#     print("\nChoose an operation:")
#     print("1. Push")
#     print("2. Pop")
#     print("3. Get stack size")
#     print("4. Exit")

#     choice = int(input("Enter your choice"))

#     if choice == 1:
#         item = input("Enter a new element ")
#         s.push(item)
#         print(f"'{item}' pushed to stack.")
#     elif choice == 2:
#         popped_item = s.pop()
#         print(f"Popped item: {popped_item}")
#     elif choice == 3:
#         print(f"Current stack size: {s.size()}")
#     elif choice == 4:
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice! Please enter a valid option.")
        


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    
q = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue (Add an element)")
    print("2. Dequeue (Remove an element)")
    print("3. Display Queue Size")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to enqueue: ")
        q.enqueue(item)
        print(f"Enqueued: {item}")
    
    elif choice == 2:
        removed_item = q.dequeue()
        if removed_item is None:
            print("Queue is empty! Cannot dequeue.")
        else:
            print(f"Dequeued: {removed_item}")

    elif choice == 3:
        print(f"Queue size: {q.size()}")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")