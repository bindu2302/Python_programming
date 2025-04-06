class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def display(self):
        print("Queue: ", self.queue)

q = Queue()
while(True):
    print("\nQueue Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Size")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter a choice (1-5): ")

    if choice == '1':
        item = input("Enter an item: ")
        q.enqueue(item)

    elif choice == '2':
        q.dequeue()
    elif choice == '3':
        print("Queue size:", q.size())
    elif choice == '4':
        q.display()
    elif choice == '5':
        print("Exiting ...")
        break
    else:
        print("Choice is invalid..")
