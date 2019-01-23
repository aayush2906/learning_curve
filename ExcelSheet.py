t=int(input())
import math
def func():
    n=int(input())
    a=[]
    while(n!=0):
        r=n%26
        val=chr(ord("A")+r-1)
        if(val=="@" and r==0):
            val="Z"
        elif(val=="@"):
            val="A"
        a.append(val)
        
        n/=26
        n=math.ceil(n-1)
        n=int(n)
    rev=a[::-1]
    for i in rev:
        print(i,end="")
    print()

for i in range(t):
    func()
