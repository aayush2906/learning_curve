def factors(n):
    f_list=[]
    for i in range(1,n+1):
        if n%i==0:
            f_list=f_list+[i]
    return(f_list)
n=int(input("number::"))
print("factors are",+factors(n))
