def isArmstrong(num):
    temp=0
    x=len(str(num))

    for i in str(num):
        temp=int(i)**x+temp

    if temp==num:
        print("Armstrong no.")
    else:
        print("not a Armstrong no:")
n=int(input("Enter the number::"))
isArmstrong(n)

'''
Armstrong Numbers: n digit no. equal to sum of nth power
of its digits
for eg: let n=153, then pow(1,3)+pow(5,3)+pow(3,3)=153
therefore armstrong no.
'''
