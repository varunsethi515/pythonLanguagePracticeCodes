def factorial_number(num):
    f=1
    if num==0:
        print(1)
    elif num>0:
        for i in range(1, num + 1):
            f=f*i
        print(f)
    elif num<0:
        if num%2==0:
            for i in range(1, num + 1):
                f = f * i
            print(f)
        elif num%2!=0:
            for i in range(1, num + 1):
                f = f * i
            print(f*-1)
#FACTORIAL DOESNOT EXIST FOR NEGATIVE INTEGERS
number=int(input("Enter the number whose factorial you want to calculate:"))
factorial_number(number)

#FACTORIAL OF A NUMBER BY USING RECURSION
def factorial(num):
    if num==0:
        return 1
    f=num*factorial(num-1)
    return f
result=factorial(5)
print(result)