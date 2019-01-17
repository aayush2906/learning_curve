'''
p
py
pyt
pyth
pytho
python
'''
string=input("Enter String")
n=len(string)
for i in range(n):
    for j in range(n):
        if(j<=i):
            print(string[j],end="");
        else:
            print(" ",end=" ");
    print()
         
