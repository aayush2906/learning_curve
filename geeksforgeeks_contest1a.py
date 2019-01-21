{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        a=int(input())
        print(digitsSum(a))
        testcases-=1
        
if __name__=='__main__':
    main()
}


#User function Template for python3
def digitsSum(n):
    a=str(n)
    a.split();
    return(int(a[0])+int(a[1]))
    
    ''' given 25
     function should return 2+5=7'''
