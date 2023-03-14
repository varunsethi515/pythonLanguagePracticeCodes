result=[]
scorelist=[]
n=int(input("Enter number of elements"))
for i in range(n):
    names=input("names")
    score=float(input("score"))
    result+=[[name,score]]
    score+=[score]
b=sorted(list(set(scorelist)))[1]
for a,c in sorted(result):
    if c==b:
        print(a)
