print()
print("Prime Numbers")
print()
num = int(input("Enter the number of your choice"))
count=1
for i in range(2,num+1):
    num%i==0
    count=count+1
if count==2:
    print("The number you have enterd is the prime number")
else:
    print("The number that you have enterd is not a prime number")
