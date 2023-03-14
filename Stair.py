def stair_case(n):
    for i in range (0,n):
        for j in range (0,n):
            if i+j >= n-1:
                print("#",end=' ')
            else:
                print(" ",end=' ')
        print("/r")
if __name__ == '__main__':
    n=input(int())
    stair_case()
