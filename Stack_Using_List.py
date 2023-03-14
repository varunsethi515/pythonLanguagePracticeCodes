stack = []
def push():
    element = input("Enter the element you want to insert in the stack")
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("Stack is empty!! plz fill it before removing")
    else:
        remove = stack.pop()
        print("Removed element is: ",remove)
        print(stack)
while True:
    print("Chose the operation you want to perfom over stack")
    print("1 for push")
    print("2 for pop")
    print("3 to exit")
    choice = int(input())
    if choice ==1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Sorry! Invalid option selected")
