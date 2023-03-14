#User Define array

from array import *
arr=array('i',[])
length=int(input("Enter the length of the array you want to create:"))
for i in range(0,length):
    element=int(input("Enter value:"))
    arr.append(element)
print(arr)

#manual search
k=0
search=int(input("Enter the element you want to search for:"))
for j in arr:
    if j==search:
        print(k)
        break
    k+=1

#inbuilt search
print(arr.index(search))
