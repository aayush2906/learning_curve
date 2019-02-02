{
#Initial Template for Python 3

def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        single=int(input())
        multivar(single,4,5,6,7) ## The single argument and multiarguments are passed to multivar function
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def multivar(a, *var):
    sum=0;
    for i in var:
        sum=sum+i
    
    print(sum+a)##print the sum of a+elements of var
    
