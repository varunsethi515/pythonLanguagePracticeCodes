list1=[2,3,4,5]
list_prime=[]
for i in list1:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
            else:
                list_prime.append(i)
                i+=1
print(list_prime)
print(len(list_prime))
