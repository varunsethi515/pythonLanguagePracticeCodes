def count_prime(list1):
    list_prime = []
    for i in list1:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    list_prime.append(i)
                    i += 1
    print(list_prime)
    print(len(list_prime))
num=int(input("Enter the number of elements you want to have in your list:"))
list_sample=[]
for i in range(num):
    element=int(input("Enter the element of your choice:"))
    list_sample.append(element)
count_prime(list_sample)
