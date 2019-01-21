{
    
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        d=int(input()) ##taking d as input
        m=int(input()) ## taking mean of 3 numbers
        print(mean(d,m))
        testcases-=1
        
if __name__=='__main__':
    main()
}

#User function Template for python3
def mean(d,m):
     return(((m*3)+d)//4)
