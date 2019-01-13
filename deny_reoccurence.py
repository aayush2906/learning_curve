l=[]  
a=[] 
n=int(input("enter size of the list"))
for i in range(0,n):
    x=int(input("enter integer"))
    l.insert(i,x)
for i in range(0,n):
    if l[i] in l:
        if l[i] not in a:
            a.insert(i,l[i])
print(a)
