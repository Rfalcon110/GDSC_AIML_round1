class StackFloat:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "underflow"

    def print_stack(self):
        for element in self.stack:
            print(f"{element:.4f}")

working=True
stack= StackFloat()
while working:
        print("\nChoose an operation:")
        print("1. Push an element")
        print("2. Pop an element")
        print("3. Print all elements")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice=="1":
            value=float(input("enter the value to be pushed"))
            stack.push(value)
        elif choice == "2":
            popped_element = stack.pop()
            if popped_element == "underflow":
                print("Underflow: Cannot pop from an empty stack.")
            else:
                print(f"Popped element: {popped_element:.4f}")
        elif choice == "3":
            print("Elements in the stack:")
            stack.print_stack()
        elif choice == "4":
            break
