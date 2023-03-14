def count_even_odd(list_sample):
    even=0
    odd=0
    for i in list_sample:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return(even,odd)

num=int(input("Enter the number of elements you want to have in your list:"))
list_sample=[]
for i in range(num):
    element=int(input("Enter the element of your choice:"))
    list_sample.append(element)
print(list_sample)
even , odd = count_even_odd(list_sample)
print("Even elements in the list: {} and Odd elements in the list: {} ".format(even , odd))
