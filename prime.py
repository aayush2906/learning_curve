def prime(n):
    temp="off"
    for i in range(2,n//2):
        if n%i==0:
            print("non-prime")
            temp="on";
            break;
    if temp=="off":
        print("prime")

n=int(input("number::"))
if n==0 or n==1:
    print("neither prime nor composite")
else:
    prime(n)
