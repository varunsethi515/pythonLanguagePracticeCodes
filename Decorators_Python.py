# Decorator is the addtional function which will be introduce in the code
# If we want to perform some modification in the code without modifying the original function

def div(a,b):
    print(a/b)

def smart_div_function(func):
    def inner_function(a,b):
        if a<b:
            a,b=b,a
        return(func(a,b))
    return(inner_function)

div1=smart_div_function(div)
div1(2,4)

# Que: IF THE NUMERATOR IS GREATER THAN DENOMINATOR, SQUARE THE DENOMINATOR BEFORE PERFORMING ADDITION
def addition(a,b):
    print(a+b)
def smart_addition_function(func):
    def inner_function(a,b):
        if a>b:
            b=b**2
        return(func(a,b))
    return(inner_function)

addition1 = smart_addition_function(addition)
addition1(3,2)

# Que: IF THE NUMERATOR IS SMALLER THAN DENOMINATOR, CUBE THE NUMERATOR BEFORE PERFORMING ADDITION
def addition(a,b):
    print(a+b)
def smart_addition_function(func):
    def inner_function(a,b):
        if a<b:
            a=a**3
        return(func(a,b))
    return(inner_function)
addition1=smart_addition_function(addition)
addition1(2,3)

#Que: IF FIRST NUMBER IS MULTIPLE OF 3 THAN TAKE THE SQUARE OF THAT NUMBER AND MULTIPLY IT WITH TH ESECOND NUMBER
def multiplication(a,b):
    print(a*b)
def smart_multiplication_function(func):
    def inner_function(a,b):
        if a%3==0:
            a=a**2
        return(func(a,b))
    return(inner_function)
multiplication1=smart_multiplication_function(multiplication)
multiplication1(3,5)