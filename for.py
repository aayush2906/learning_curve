'''
You are given a number N, you need to print its multiplication table.
'''
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        numbah=int(input())
        multiplicationTable(numbah)
        print()
        testcases-=1
        
if __name__=='__main__':
    main()
}

def multiplicationTable(N):
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i*N, end=" ") 
