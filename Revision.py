#1. WAP to calculate the Factorial of any number
num = int(input("Enter any number"))
fact =1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of a given number is",fact)

#2. WAP to chect weather the number is plaindrome or not
num=int(input("Enter the number to be checked"))
s=0
temp=num
while (num>0):
    r=num%10
    s=s*10+r
    num = num//10
if temp==s:
    print("Number that you have entered is Plaindrome Number")
else:
    print("Number that you have entered is not a Plaindrome Number")

#3.WAP to check weather the number is Armstrong Number or Not
num=int(input("Enter the number to be checked"))
temp = num
s=0
while(num!=0):
    r=num%10
    s=s+(r*r*r)
    num=num//10
if temp==s:
    print("Number that you have entered is Armstrong Number")
else:
    print("Number you have entered is not an Armstrong Number")

#While using for loop in case of dictionary ".items()" is used with the name of dictionary to fectch all the key value pair in the form of tuples
#eg=>"for i in dictionary_sample.items():"


