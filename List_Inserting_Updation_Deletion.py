def inserting_list(list_sample):
    print("Inserting an element in the list")
    length=int(input("Enter the number of elements you want to add in the list"))
    for i in range(length):
        element = input("Enter the element that you want to add in the list")
        list_sample.append(element)
    print(list_sample)
def removing_list(list_sample):
    print("Removing an element from the List")
    element=input("Enter the element that you want to remove from the list")
    list_sample.remove(element)
    print(list_sample)

list_sample=[]
choice= int(input("Enter the operation that you want to perform (0 to EXIT!!, 1 for Inserting and 2 for Removing)"))
if choice == 1:
    inserting_list(list_sample)
elif choice == 2:
    removing_list(list_sample)


